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
from comunidade.forms import FormLogin, FormCriarConta
from comunidade.models import Usuario, Post
from flask_login import (
    login_user, 
    logout_user, 
    current_user,
    login_required)


@app.route("/")
@login_required
def home():
    return render_template("home.html")


@app.route("/contato")
def contato():
    return render_template("contato.html")


@app.route("/usuarios")
@login_required
def usuarios():
    lista_usuarios:list = ["Lira", "João", "Alon", "Alessandra", "Amanda"]
    
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
    return render_template("perfil.html")


@app.route("/post/criar")
@login_required
def criar_post():
    return render_template("criarpost.html")

