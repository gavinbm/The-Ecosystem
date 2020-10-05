from flask import Flask, redirect, url_for, render_template, request, session, flash
from flask_sqlalchemy import SQLAlchemy

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

@app.route("/", methods = ["POST", "GET"])
def home():
    render_template("index.html")
    if request.method == "POST":
        name = request.form["nm"]
        password = request.form["pw"]
        session["user"] = name
        found_user = users.query.filter_by(name = name).first()
        if found_user:
            return redirect(url_for("games"))
        else:
            if check_password(Specials, password):
                usr = users(name, "")
                db.session.add(usr)
                db.session.commit()
                return redirect(url_for("games"))
            else:
                error = "Invalid username or password, please try again"
                return render_template("index.html", error=error)
    else:
        return render_template("index.html")

@app.route("/games", methods=["POST", "GET"])
def games():
    if "user" in session:
        user = session["user"]
        flash("Welcome Back " + user + " :D")
    return render_template("games.html")

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
