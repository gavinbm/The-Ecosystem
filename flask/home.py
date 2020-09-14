from helpers import *

@app.route("/", methods = ["POST", "GET"])
def home():
    render_template("index.html")
    if request.method == "POST":
        name = request.form["nm"]
        password = request.form["pw"]
        if find_user(Users, name, password):
            session["user"] = name
            return redirect(url_for("games"))
        else:
            if check_username(Users, name) and check_password(Specials, password):
                create_user(name, password)
            else:
                return render_template("index.html")
    else:
        return render_template("index.html")

@app.route("/games", methods=["POST", "GET"])
def games():
    if "user" in session:
        user = session["user"]
        flash(f"Welcome Back {user} :D")
    return render_template("games.html")

if __name__ == "__main__":
    app.run(debug=True)
