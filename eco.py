from webApp import app
from helpers import *

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
        flash(f"Welcome Back {user} :D")
    return render_template("games.html")

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)