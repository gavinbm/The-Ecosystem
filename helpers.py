from flask import Flask, redirect, url_for, render_template, request, session, flash
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message

#from webApp import app
app = Flask(__name__)
app.secret_key = "howdy"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

mail= Mail(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'ecosystemnewsletter@gmail.com'
app.config['MAIL_PASSWORD'] = '@PYp$=;NnZc;689:'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

class users(db.Model):
    _id = db.Column("id", db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    password = db.Column(db.String(100))

    def __init__(self, name, password):
        self.name = name
        self.password = password


# Special chars for passwords
Specials = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-']

# Ensures a secure password
def check_password(Specials, password):
    if len(password) < 8:
        return False
    if not any(char.isdigit() for char in password) or not any(char in Specials for char in password):
        return False
    if not any(char.isupper() for char in password) or not any(char.islower() for char in password):
        return False
    else:
        return True
