from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.user import User
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

@app.route("/")
def index():
    return render_template("splash.html")

@app.route("/register", methods=["POST"])
def register():
    if not User.validate_register(request.form):
        return redirect("/")
    data = {
        "username": request.form["username"],
        "email": request.form["email"],
        "password": bcrypt.generate_password_hash(request.form["password"]),
    }
    id = User.save(data)
    session["user_id"] = id
    flash("Registration successful! Welcome, {}!".format(request.form["first_name"]), "success")
    return redirect("/dashboard")

@app.route("/user")
def user_profile():
    if "user_id" not in session:
        return redirect("/")
    
    user = User.get_user_by_id({"id": session["user_id"]})

    return render_template("dashboard.html", user=user)

@app.route("/login", methods=["POST"])
def login():
    user = User.get_user_by_email(request.form)
    if not user:
        flash ("Invalid Email/Password", "login")
        return redirect ("/")
    if not bcrypt.check_password_hash(user.password, request.form["password"]):
        flash("Invalid Email/Password", "login")
        return redirect ("/")
    session["user_id"] = user.id
    return redirect("/dashboard")

@app.route("/logout", methods=["POST"])
def logout():
    session.clear()
    return redirect("/")