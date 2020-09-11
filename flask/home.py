from flask import Flask, redirect, url_for, render_template, request
import json

app = Flask(__name__)

with open("accounts.json") as f:
    Users = json.load(f)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/make", methods=["POST", "GET"])
def make():
     if request.method == "POST":
         name = request.form["nm"]
         password = request.form["pw"]
         pass_conf = request.form["pw2"]
         if check_password(Specials, password, pass_conf) and check_username(Users, name):
             user = {"name": name, "password": password, "status": 1}
             Users.append(user)
         with open("accounts.txt", "w") as fout:
             json.dump(Users, fout)
         return redirect(url_for("user", name=name))
     else:
         return render_template("make.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        name = request.form["nm"]
        password = request.form["pw"]
        check = False
        for user in Users:
            if user["name"] == name and user["password"] == password:
                check = True
                user["status"] = 1
                with open("accounts.txt", "w") as fout:
                    json.dump(Users, fout)
                return redirect(url_for("user", name=name))
        if not check:
            return render_template("login.html")
    else:
        return render_template("login.html")

@app.route("/<name>")
def user(name):
    return f"Hello {name}!"

@app.route("/admin")
def admin():
    return redirect(url_for("user", name="root"))

if __name__ == "__main__":
    app.run(debug=True)
