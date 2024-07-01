from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)

app.config['SECRET_KEY'] = "79d1cac6cd1f7aeff9c5988f730a1df7"
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///comunidade.db"

database = SQLAlchemy(app)

bcrypt = Bcrypt(app)

from comunidade import routes