from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.user import User
from flask_bcrypt import bcrypt

@app.route("/register", methods=["POST"])
def register():
    if not User.validate_user(request.form):
        return redirect('/login_and_registration')
    salt = bcrypt.gensalt()
    pw_hash = bcrypt.hashpw(request.form['password'].encode('utf-8'),salt)
    data = {
        'username':request.form['username'],
        'email':request.form['email'],
        'password':pw_hash
    }
    new_user = User.register(data)
    session['user_id'] = new_user
    session['is_logged'] = True
    return redirect('/dashboard')

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
        return redirect ("/log_and_reg")
    if not bcrypt.check_password_hash(user.password, request.form["password"]):
        flash("Invalid Email/Password", "login")
        return redirect ("/log_and_reg")
    session["user_id"] = user.id
    return redirect("/dashboard")

@app.route("/logout", methods=["POST"])
def logout():
    session.clear()
    return redirect("/")