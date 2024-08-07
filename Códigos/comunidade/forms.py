from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import (
    StringField, 
    PasswordField, 
    SubmitField,
    BooleanField,
    TextAreaField)
from wtforms.validators import (
    DataRequired, 
    Email, 
    Length, 
    EqualTo,
    ValidationError)
from comunidade.models import Usuario
from flask_login import current_user


class FormCriarConta(FlaskForm):
    username:StringField = StringField("Nome de Usuário", validators=[DataRequired()])
    email:StringField = StringField("E-mail", validators=[DataRequired(), Email()])
    senha:StringField = PasswordField("Senha", validators=[DataRequired(), Length(6, 20)])
    confirmacao_senha:PasswordField = PasswordField("Confirmação da Senha", validators=[DataRequired(), Length(6, 20), EqualTo("senha")])
    botao_submit_criarconta = SubmitField("Criar Conta")
    
    # caso queira fazer um validador personalizado faça um método começando com validate_, isso é uma abstração do flask
    def validate_username(self, username):
        usuario_username:Usuario = Usuario.query.filter_by(username=username.data).first()
        
        if usuario_username:
            raise ValidationError("Usuário já cadastrado. Cadastre-se com outro ou faça login!")
    
    def validate_email(self, email):
        usuario_email = Usuario.query.filter_by(email=email.data).first()
        
        if usuario_email:
            raise ValidationError("E-mail já cadastrado. Cadastre-se com outro ou faça login para continuar!")


class FormLogin(FlaskForm):
    email:StringField = StringField("E-mail", validators=[DataRequired(), Email()])
    senha:PasswordField = PasswordField("Senha", validators=[DataRequired(), Length(6, 20)])
    lembrar_dados:BooleanField = BooleanField("Lembrar Dados de Acesso")
    botao_submit_login = SubmitField("Fazer Login")
    

class FormEditarPerfil(FlaskForm):
    username:StringField = StringField("Nome de Usuário", validators=[DataRequired()])
    email:StringField = StringField("E-mail", validators=[DataRequired(), Email()])
    foto_perfil:FileField = FileField("Atualizar Foto de Perfil", validators=[FileAllowed(["jpg", "png"])])
    curso_excel:BooleanField = BooleanField("Excel Impressionador")
    curso_vba:BooleanField = BooleanField("VBA Impressionador")
    curso_powerbi:BooleanField = BooleanField("Power BI Impressionador")
    curso_python:BooleanField = BooleanField("Python Impressionador")
    curso_javascript:BooleanField = BooleanField("JavaScript Impressionador")
    curso_sql:BooleanField = BooleanField("SQL Impressionador")

    botao_submit_editarperfil = SubmitField("Confirmar Edição")
    
    def validate_username(self, username):
        if current_user.username != username.data:
            usuario_username:Usuario = Usuario.query.filter_by(username=username.data).first()
            
            if usuario_username:
                raise ValidationError("Já existe um usuário com esse nome. Cadastre outro nome de usuário!")
    
    def validate_email(self, email):
        if current_user.email != email.data:
            # verificar se o usuario mudou de email
            usuario_email = Usuario.query.filter_by(email=email.data).first()
            
            if usuario_email:
                raise ValidationError("Já existe um usuário com esse email. Cadastre outro email!")


class FormCriarPost(FlaskForm):
    titulo:StringField = StringField("Título do Post", validators=[DataRequired(), Length(2, 140)])
    corpo:TextAreaField = TextAreaField("Escreva seu Post aqui!", validators=[DataRequired()])
    botao_submit_criar_post:SubmitField = SubmitField("Enviar Post")