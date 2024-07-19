import os
from secrets import token_hex
from PIL import Image
from comunidade import (
    app, 
    database, 
    bcrypt)
from flask import (
    render_template, 
    url_for,
    request,
    flash,
    redirect,)
from comunidade.forms import (
    FormLogin, 
    FormCriarConta, 
    FormEditarPerfil,
    FormCriarPost)
from comunidade.models import Usuario, Post
from flask_login import (
    login_user, 
    logout_user, 
    current_user,
    login_required)


@app.route("/")
def home():
    posts:list = Post.query.order_by(Post.id.desc())
    
    return render_template("home.html", posts=posts)


@app.route("/contato")
def contato():
    return render_template("contato.html")


@app.route("/usuarios")
@login_required
def usuarios():
    lista_usuarios:list = Usuario.query.all()
    
    return render_template("usuarios.html", lista_usuarios=lista_usuarios)


@app.route("/login", methods=["GET", "POST"])
def login():
    form_login:FormLogin = FormLogin()
    
    form_criarconta:FormCriarConta = FormCriarConta()
    
    if form_login.validate_on_submit() and "botao_submit_login" in request.form:
        usuario:Usuario = Usuario.query.filter_by(email=form_login.email.data).first()
        
        if usuario and bcrypt.check_password_hash(usuario.senha, form_criarconta.senha.data):
            login_user(usuario, remember=form_login.lembrar_dados.data)
            
            flash(f"Login feito com sucesso no e-mail: {form_login.email.data}", "alert-success")

            parametro_next = request.args.get('next')
            
            if parametro_next:
                return redirect(parametro_next)
            else:
                return redirect(url_for("home"))
        else:
            flash(f"Falha no Login. E-mail ou Senha Incorretos", "alert-danger")
        
    if form_criarconta.validate_on_submit() and "botao_submit_criarconta" in request.form:
        flash(f"Conta criada para o e-mail: {form_criarconta.email.data}", "alert-success")
        
        senha_cript = bcrypt.generate_password_hash(form_criarconta.senha.data)
        
        usuario:Usuario = Usuario(
            username=form_criarconta.username.data, 
            email=form_criarconta.email.data, 
            senha=senha_cript)
        
        database.session.add(usuario)
        
        database.session.commit()
        
        return redirect(url_for("home"))
    
    return render_template("login.html", form_login=form_login, form_criarconta=form_criarconta)


@app.route("/sair")
@login_required
def sair():
    logout_user()
    flash(f"Logout Feito com Sucesso", "alert-info")
    
    return redirect(url_for("home"))


@app.route("/perfil")
@login_required
def perfil():
    foto_perfil = url_for('static', filename=f'fotos_perfil/{current_user.foto_perfil}')
    
    return render_template("perfil.html", foto_perfil=foto_perfil)


@app.route("/post/criar", methods=["GET", "POST"])
@login_required
def criar_post():
    
    form_criar_post = FormCriarPost()
    
    if form_criar_post.validate_on_submit():
        post = Post(
            titulo=form_criar_post.titulo.data,
            corpo=form_criar_post.corpo.data,
            autor=current_user)
        
        database.session.add(post)
        
        database.session.commit()
        
        flash(f"Post Criado com Sucesso", "alert-success")
        
        return redirect(url_for("home"))
    
    return render_template("criarpost.html", form_criar_post=form_criar_post)


def salvar_imagem(imagem:str) -> str:
    codigo = token_hex(8)
    
    nome, extensao = os.path.splitext(imagem.filename)
    
    nome_arquivo = nome + codigo + extensao
    
    caminho_completo = os.path.join(app.root_path, 'static', 'fotos_perfil', nome_arquivo)
    
    tamanho_imagem = (200, 200)
    
    imagem_reduzida = Image.open(imagem)
    
    imagem_reduzida.thumbnail(tamanho_imagem)
    
    imagem_reduzida.save(caminho_completo)
    
    return nome_arquivo


def atualizar_cursos(form_editarperfil:FormEditarPerfil) -> str:
    lista_cursos = list()
    
    for campo in form_editarperfil:
        if "curso_" in campo.name and campo.data:
            lista_cursos.append(campo.label.text)
            
    return ";".join(lista_cursos)


@app.route("/perfil/editar", methods=["GET", "POST"])
@login_required
def editar_perfil():
    form_editarperfil = FormEditarPerfil()
    
    if form_editarperfil.validate_on_submit():
        current_user.email = form_editarperfil.email.data
        
        current_user.username = form_editarperfil.username.data
        
        if form_editarperfil.foto_perfil.data:
            nome_imagem = salvar_imagem(form_editarperfil.foto_perfil.data)
            
            current_user.foto_perfil = nome_imagem
            
        current_user.cursos = atualizar_cursos(form_editarperfil)
        
        database.session.commit()
        
        flash(f"Perfil Atualizado com Sucesso!", "alert-success")
        
        return redirect(url_for("perfil"))
    elif request.method == "GET":
        form_editarperfil.email.data = current_user.email
        
        form_editarperfil.username.data = current_user.username
    
    foto_perfil = url_for('static', filename=f'fotos_perfil/{current_user.foto_perfil}')
    
    return render_template('editarperfil.html', foto_perfil=foto_perfil, form_editarperfil=form_editarperfil)


@app.route("/post/<post_id>", methods=["GET", "POST"])
@login_required
def exibir_post(post_id):
    post = Post.query.get(post_id)
    
    if current_user == post.autor:
        form_editar_post:FormCriarPost = FormCriarPost()
        
        if form_editar_post.validate_on_submit():
            post.titulo = form_editar_post.titulo.data
            
            post.corpo = form_editar_post.corpo.data
            
            database.session.commit()
            
            flash(f"Post Atualizado com Sucesso!", "alert-success")
            
            return redirect(url_for("home"))
        elif request.method == "GET":
            form_editar_post.titulo.data = post.titulo
            
            form_editar_post.corpo.data = post.corpo
            
        return render_template("post.html", post=post, form_editar_post=form_editar_post)
    
    return render_template("post.html", post=post)