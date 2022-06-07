from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta
from flask_mysqldb import MySQL, MySQLdb
from flask_sqlalchemy import SQLAlchemy



# create a flask instance
app = Flask(__name__)
# secret key
app.secret_key = "IUYijhLKIUyLkj"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://py_xavier:pk6pMJXXj83n@185.115.218.166/py_xavier'
# add database
app.config['MYSQL_HOST'] = '185.115.218.166'
app.config['MYSQL_USER'] = 'py_xavier'
app.config['MYSQL_PASSWORD'] = 'pk6pMJXXj83n'
app.config['MYSQL_DB'] = 'py_xavier'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

db = SQLAlchemy(app)
db2 = MySQL(app)

cities=[]

class users(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    password = db.Column(db.String(50))
    password_check = db.Column(db.String(50))

    def __init__(self, name, email):
        self.name = name
        self.email = email


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/compare", methods=["POST", "GET"])
def compare():
    cur = db2.connection.cursor(MySQLdb.cursors.DictCursor)
    cur.execute("SELECT name_climate FROM city order by name_climate")
    citylist = cur.fetchall()

    # Get City Values
    if request.method == "POST":
        city1 = request.form.get("city1")
        city2 = request.form.get("city2")
        return redirect(url_for("dashboard"))

    return render_template("compare.html", citylist=citylist)






@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/login", methods=["GET", "POST"])
def login():

    # # POST
    # if request.method == "POST": # na het verzenden van inloggegevens
    #
    #     # user opslaan in de sessie
    #     post_user = request.form["nm"]
    #     session.permanent = True
    #     session["user"] = post_user
    #
    #     # gebruiker opzoeken in de database
    #     found_user = users.query.filter_by(name=post_user).first()
    #
    #     # gebruiker bestaat al
    #     if found_user:
    #         session["email"] = found_user.email
    #
    #     # gebruiker bestaat nog niet
    #     else:
    #         # gebruiker aanmaken in de database
    #         usr = users(post_user, "")
    #         db.session.add(usr)
    #         db.session.commit()
    #
    #     flash(f"Login successful!")
    #     return redirect(url_for("welcome_user"))
    #
    # # GET
    # else:  # na het opvragen van het inlogformulier
    #
    #     # gebruiker is al ingelogd
    #     if "user" in session:
    #         flash(f"Already logged in!")
    #         return redirect(url_for("welcome_user"))
    #
    #     # gebruiker is nog niet ingelogd
        return render_template("signin.html")


@app.route("/user", methods=["GET", "POST"])
def welcome_user():

    # als de gebruiker ingelogd is
    if "user" in session:
        user = session["user"]

        if request.method == "POST": # als de gebruiker zijn email opstuurt

            # email opslaan in sessie
            email = request.form["email"]
            session["email"] = email

            # gebruiker opzoeken in de database, en updaten
            found_user = users.query.filter_by(name=user).first()
            found_user.email = email
            db.session.commit()

            flash("Email was saved")

        elif "email" in session:
            email = session["email"]

        else:
            email = None

        return render_template("user.html", email=email)

    # als de gebruiker NIET ingelogd is
    else:
        flash(f"You are not logged in!")
        return redirect(url_for("login"))



@app.route("/logout")
def logout():
    session.pop("user", None)
    session.pop("email", None)
    flash( f"You have been logged out!", "info" )
    return redirect(url_for("login"))


@app.route("/admin")
def admin():
    return redirect(url_for("user", name="Admin!"))


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
