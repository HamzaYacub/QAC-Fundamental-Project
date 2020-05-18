from flask import Flask
from os import getenv
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']=getenv('CAR_HIRE_DB_URI')
app.config['SECRET_KEY']=getenv('SECRET_KEY')
app.config['WTF_CSRF_SECRET_KEY']=getenv('CSRF_SECRET_KEY')
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
csrf = CSRFProtect(app)
csrf.init_app(app)

from application import routes
