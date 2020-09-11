from helpers import *

@app.route("/", methods = ["POST", "GET"])
def home():
    render_template("index.html")
    if request.method == "POST":
        name = request.form["nm"]
        password = request.form["pw"]
        if find_user(Users, name, password):
            flash("Welcome Back Friend :D")
        else:
            if check_username(Users, name) and check_password(Specials, password):
                create_user(name, password)
            else:
                return render_template("index.html")
    else:
        return render_template("index.html")

@app.route("/make", methods=["POST", "GET"])
def make():
     if request.method == "POST":
         name = request.form["nm"]
         password = request.form["pw"]
         if check_password(Specials, password, pass_conf) and check_username(Users, name):
             user = {"name": name, "password": password, "status": 1, "gamesplayed":[]}
             Users.append(user)
         with open("accounts.txt", "w") as fout:
             json.dump(Users, fout)
         return redirect(url_for("user", name=name))
     else:
         return render_template("make.html")

if __name__ == "__main__":
    app.run(debug=True)
