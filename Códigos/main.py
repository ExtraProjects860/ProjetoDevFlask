from flask import (
    Flask, 
    render_template, 
    url_for,
    request,
    flash,
    redirect
    )
from forms import FormLogin, FormCriarConta


app = Flask(__name__)

app.config['SECRET_KEY'] = "79d1cac6cd1f7aeff9c5988f730a1df7"


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/contato")
def contato():
    return render_template("contato.html")


@app.route("/usuarios")
def usuarios():
    lista_usuarios:list = ["Lira", "João", "Alon", "Alessandra", "Amanda"]
    
    return render_template("usuarios.html", lista_usuarios=lista_usuarios)


@app.route("/login", methods=["GET", "POST"])
def login():
    form_login:FormLogin = FormLogin()
    
    form_criarconta:FormCriarConta = FormCriarConta()
    
    if form_login.validate_on_submit() and "botao_submit_login" in request.form:
        flash(f"Login feito com sucesso no e-mail: {form_login.email.data}", "alert-success")
        
        return redirect(url_for("home"))
        
    if form_criarconta.validate_on_submit() and "botao_submit_criarconta" in request.form:
        flash(f"Conta criada para o e-mail: {form_criarconta.email.data}", "alert-success")
        
        return redirect(url_for("home"))
    
    return render_template("login.html", form_login=form_login, form_criarconta=form_criarconta)


if __name__ == "__main__":
    app.run(debug=True)