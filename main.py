from flask import Flask, abort, flash, render_template, redirect, request, url_for
from flask_bootstrap import Bootstrap
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from datetime import datetime
from forms import CafeForm, LoginForm, RegisterForm
import os

# Constants
CURRENT_YEAR = datetime.now().year
print(CURRENT_YEAR)

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
Bootstrap(app)

# CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Login Manager
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# CONFIGURE TABLES
class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))


class Cafes(db.Model):
    __tablename__ = "cafes"
    id = db.Column(db.Integer, primary_key=True)
    cafe = db.Column(db.String(100))
    location = db.Column(db.String(250))
    open_time = db.Column(db.String(8))
    close_time = db.Column(db.String(8))
    rating = db.Column(db.String(5))
    wifi = db.Column(db.String(5))
    power = db.Column(db.String(5))


# db.create_all()


@app.route('/')
def home():
    return render_template('index.html', year=CURRENT_YEAR)


@app.route('/cafes')
def cafes():
    form = CafeForm()
    return render_template('cafes.html', year=CURRENT_YEAR)


@app.route('/login')
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        user = User.query.filter_by(email=email).first()
        if not user:
            flash("That email does not exist, please try again.")
            return redirect(url_for("login"))
        # Password Incorrect
        elif not check_password_hash(user.password, password):
            flash('Password incorrect, please try again.')
            return redirect(url_for('login'))
        # Email exists and password correct
        else:
            login_user(user)
            return redirect(url_for('get_all_posts'))
    return render_template("login.html", form=form, current_user=current_user, year=CURRENT_YEAR)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('get_all_posts'))


@app.route('/add')
def add_cafe():
    pass


if __name__ == '__main__':
    app.run(debug=True)

