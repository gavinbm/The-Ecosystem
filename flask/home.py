from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["nm"]
        return redirect(url_for("user", name=user))
    else:
        return render_template("login.html")

@app.route("/<name>")
def user(name):
    return f"Hello {name}!"

app.route("/admin")
def admin():
    return redirect(url_for("user", name="root"))

if __name__ == "__main__":
    app.run(debug=True)
