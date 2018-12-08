from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user

from application import app, db
from application.auth.models import User
from application.auth.forms import LoginForm
from application.auth.forms import RegistrationForm

from sqlalchemy.exc import IntegrityError

@app.route("/auth/login", methods=["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form = LoginForm())

    form = LoginForm(request.form)

    user = User.query.filter_by(username=form.username.data, password=form.password.data).first()
    if not user:
        return render_template("auth/loginform.html", form = form,
                               error = "No such username or password")


    login_user(user)
    return redirect(url_for("index"))

@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))

@app.route("/auth/register/")
def auth_register():
    return render_template("auth/registrationform.html", form = RegistrationForm())

@app.route("/auth/create/", methods=["POST"])
def user_create():
    form = RegistrationForm(request.form)

    if not form.validate():
        return render_template("auth/registrationform.html", form = form)

    u = User(form.name.data, form.username.data, form.password.data)
    db.session().add(u)

    try:
        db.session().commit()
    except IntegrityError:
        db.session.rollback()
        return render_template("auth/registrationform.html", form = form,
                               error = "An account with this username already exists")

    return redirect(url_for("index"))