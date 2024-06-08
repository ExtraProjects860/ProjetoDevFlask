from flask_wtf import FlaskForm
from wtforms import (
    StringField, 
    PasswordField, 
    SubmitField,
    BooleanField
    )
from wtforms.validators import (
    DataRequired, 
    Email, 
    Length, 
    EqualTo
    )


class FormCriarConta(FlaskForm):
    username:str = StringField("Nome de Usuário", validators=[DataRequired()])
    email:str = StringField("E-mail", validators=[DataRequired(), Email()])
    senha:str = PasswordField("Senha", validators=[DataRequired(), Length(6, 20)])
    confirmacao_senha:str = PasswordField("Confirmação da Senha", validators=[DataRequired(), Length(6, 20), EqualTo("senha")])
    botao_submit_criarconta = SubmitField("Criar Conta")


class FormLogin(FlaskForm):
    email:str = StringField("E-mail", validators=[DataRequired(), Email()])
    senha:str = PasswordField("Senha", validators=[DataRequired(), Length(6, 20)])
    lembrar_dados = BooleanField("Lembrar Dados de Acesso")
    botao_submit_login = SubmitField("Fazer Login")