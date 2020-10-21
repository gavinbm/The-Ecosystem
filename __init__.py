from flask import Flask

app = Flask(__name__)
app.secret_key = "howdy"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

import eco
