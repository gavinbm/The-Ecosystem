from helpers import *
from battleship import *


#----------------- App/mail Config -------------------#
app = Flask(__name__)
app.secret_key = "howdy"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'ecosystemnewsletter@gmail.com'
app.config['MAIL_PASSWORD'] = '@PYp$=;NnZc;689:'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

#----------------- Database -------------------#
db = SQLAlchemy(app)
db.init_app(app)

class users(db.Model):
    _id = db.Column("id", db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    password = db.Column(db.String(100))

    def __init__(self, name, password):
        self.name = name
        self.password = password

db.create_all()
#----------------- Views --------------------#
@app.route("/", methods = ["POST", "GET"])
def home():
    if request.method == "POST":
        name = request.form["nm"]
        password = request.form["pw"]
        session["user"] = name
        found_user = users.query.filter_by(name = name).first()
        if name == "" or password == "":
            flash("Please enter a valid username and password")
            return render_template("index.html")
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
    global comp, board, player
    board = makeBoard()
    comp = randShip()

    if "user" in session:
        user = session["user"]
        flash(f"Welcome Back {user} :D")

    if request.method == "POST":
        playerX = int(request.form["placeX"])
        playerY = int(request.form["placeY"])
        player = placeShip(board, playerX, playerY)

    return render_template("games.html", board=board)

@app.route("/gameLogic", methods=["POST", "GET"])
def gameLogic():
    global board, comp, player

    if request.method == "POST":
        targX = int(request.form["xin"])
        targY = int(request.form["yin"])
        if comp.pos[0] == targX and comp.pos[0] == targY:
            board[targY][targX] = "X"
            flash("Hit! You Win!")
            return render_template("games.html", board=board)
        else:
            board[targY][targX] = "M"
            flash("Miss!")
            compMove(board, player, comp)

    return render_template("games.html", board=board)

@app.route("/class", methods=["POST", "GET"])
def classStuff():
    if "user" in session:
        user = session["user"]
        flash(f"Hey there {user} :D")
    return render_template("class.html")

@app.route("/news", methods=["POST", "GET"])
def news():
    sendTo = ["ecosystemnewsletter@gmail.com"]
    if request.method == "POST":
        if request.form["userMail"] != "":
            sendTo.append(request.form["userMail"])
        if request.form["fullSend"] == "Send":
            msg = Message('Ecosystem Fun Fact!', sender = 'ecosystemnewsletter@gmail.com', recipients = sendTo)
            msg.body = "Did you know that George Washington's teeth weren't wooden? They were made out of ivory, human teeth, and metal!"
            mail.send(msg)
            flash("Message sent!")
            return render_template("news.html")
    return render_template("news.html")

if __name__ == "__main__":
    app.run(debug=True)
