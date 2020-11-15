#from webApp import app
from helpers import *

@app.route("/", methods = ["POST", "GET"])
def home():
    if request.method == "POST":
        name = request.form["nm"]
        password = request.form["pw"]
        session["user"] = name
        found_user = users.query.filter_by(name = name).first()
        if found_user:
            flash(f"Return to the Ecosystem {found_user.name}!")
            return render_template("index.html")
        else:
            if check_password(Specials, password):
                usr = users(name, password)
                db.session.add(usr)
                db.session.commit()
                flash(f"Welcome to the Ecyosystem {name}!")
                return render_template("index.html")
            else:
                error = "Invalid username or password, please try again"
                return render_template("index.html", error=error)
    else:
        return render_template("index.html")

@app.route("/games", methods=["POST", "GET"])
def games():
    if "user" in session:
        user = session["user"]
        flash(f"Welcome Back {user} :D")
    return render_template("games.html")

@app.route("/class", methods=["POST", "GET"])
def classStuff():
    if "user" in session:
        user = session["user"]
        flash(f"Hey there {user} :D")
    return render_template("class.html")

@app.route("/news", methods=["POST", "GET"])
def news():
    msg = Message('Support Ticket', sender = '[EMAIL HERE]', recipients = ['RECIPIENT HERE'])
    msg.body = "Hello Flask message sent from Flask-Mail"
    mail.send(msg)
    return render_template("news.html")

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
