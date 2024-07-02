from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app:Flask = Flask(__name__)

app.config['SECRET_KEY'] = "79d1cac6cd1f7aeff9c5988f730a1df7"
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///comunidade.db"

database:SQLAlchemy = SQLAlchemy(app)

bcrypt:Bcrypt = Bcrypt(app)

login_manager:LoginManager = LoginManager(app)
login_manager.login_view = "login"
login_manager.login_message = "Por favor faça login para acessar esta página."
login_manager.login_message_category = "alert-info"

from comunidade import routes