from flask import Flask,session,redirect,render_template,request
from flask_login import LoginManager,UserMixin,login_user,login_required,logout_user,current_user
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'unimal123'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# app.config['REMEMBER_COOKIE_DURATION'] = timedelta(seconds=15)
db = SQLAlchemy(app=app)
login = LoginManager(app)
login.login_view='login'

from app.models import *
from app.bs4 import *
from app.logical_card import *
from app.solenoid import *
from app.routes import *