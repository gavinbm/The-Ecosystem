from __init__ import *

app = Flask(__name__)
app.secret_key = "howdy"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

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
