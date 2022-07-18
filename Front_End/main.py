from flask import Flask, redirect, url_for, render_template, request, session, flash
from flask_mysqldb import MySQL, MySQLdb
from flask_sqlalchemy import SQLAlchemy
from Groepswerk_grafieken import create_graphs
import flask_login
from werkzeug.security import generate_password_hash, check_password_hash


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
login_manager = flask_login.LoginManager()
login_manager.init_app(app)


db = SQLAlchemy(app)
db2 = MySQL(app)

# the UserMixin adds properties that are used by Flask-Login on various instances.(is_authenticated(), get_id(), ...)
# Password hash functions are from the Python Werkzeug library, super easy
class User(flask_login.UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    hashed_password = db.Column(db.String(255))

    def __init__(self, name, password):
        self.name = name
        self.hashed_password = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.hashed_password, password)


# Used by Flask-login library to load users on login
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route("/")
# @flask_login.login_required
def home():
    return render_template("index.html")


@app.route("/compare", methods=["POST", "GET"])
@flask_login.login_required
def compare():
    cur = db2.connection.cursor(MySQLdb.cursors.DictCursor)
    cur.execute("SELECT name_climate FROM city order by name_climate")
    citylist = cur.fetchall()

    # Get City Values
    if request.method == "POST":
        city1 = request.form.get("city1")
        city2 = request.form.get("city2")
        create_graphs(city1, city2)
        return redirect(url_for("dashboard"))

    return render_template("compare.html", citylist=citylist)


@app.route("/dashboard")
@flask_login.login_required
def dashboard():
    return render_template("dashboard.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    # If user is logged in, redirect to homepage/whatever
    if flask_login.current_user.is_authenticated:
        return redirect("/")

    # If request is the form submit
    if request.method == 'POST':
        # Retrieve email/name from form
        name = request.form['email']
        # Query user by email/name
        user = User.query.filter_by(name=name).first()
        # If query returns something (is not None) AND passwords match (checks can be separated in different if statements for more specific error handling)
        if user is not None and user.verify_password(request.form['password']):
            # Login user & redirect to homepage/whatever
            flask_login.login_user(user)
            return redirect(url_for("compare"))
        # Else show error
        else:
            flash("Wrong login!", 'error')

    # Render login page
    return render_template('signin.html')



@app.route("/logout", methods= ['GET'])
def logout():
    # if user is logged in then logout
    if flask_login.current_user.is_authenticated:
        flask_login.logout_user()
    return redirect(url_for("login"))


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
