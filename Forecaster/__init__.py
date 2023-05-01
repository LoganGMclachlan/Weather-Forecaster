# imported modules to be used in program
from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy as SQLA
from flask_bcrypt import Bcrypt
from flask_mail import Mail
import os

# sets up forecaster app
forecaster = Flask(__name__)
forecaster.config["SECRET_KEY"] = os.environ.get("WF_SK")
database = SQLA(forecaster)
forecaster.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
login_manager = LoginManager(forecaster)
login_manager.login_view = "login"
login_manager.login_message_category = "info"
hasher = Bcrypt(forecaster)

forecaster.config["MAIL_SERVER"] = "smtp.gmail.com"
forecaster.config["MAIL_PORT"] = 587
forecaster.config["MAIL_USE_TLS"] = True
forecaster.config["MAIL_USERNAME"] = os.environ.get("ALT_EMAIL_USER")
forecaster.config["MAIL_PASSWORD"] = os.environ.get("ALT_EMAIL_PASS")
mail = Mail(forecaster)



import Forecaster.routes
