from main import database
from datetime import datetime


class Usuario(database.Model):
    id:int = database.Column(database.Integer, primary_key=True)
    username:str = database.Column(database.String, nullable=False)
    email:str = database.Column(database.String, nullable=False, unique=True)
    senha:str = database.Column(database.String, nullable=False)
    foto_perfil:str = database.Column(database.String, default="default.jpg")
    posts = database.relationship("Post", backref="autor", lazy=True)
    cursos = database.Column(database.String, nullable=False, default="Não Informado")
    

class Post(database.Model):
    id:int = database.Column(database.Integer, primary_key=True)
    titulo = database.Column(database.String, nullable=False)
    corpo = database.Column(database.Text, nullable=False)
    data_criacao = database.Column(database.DateTime, nullable=False, default=datetime.utcnow)
    id_usuario = database.Column(database.Integer, database.ForeingKey("usuario.id"), nullable=True)