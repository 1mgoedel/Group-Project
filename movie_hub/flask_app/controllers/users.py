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
    return redirect('/splash')

@app.route("/user")
def user_profile():
    if "user_id" not in session:
        return redirect("/")
    
    user = User.get_user_by_id({"id": session["user_id"]})

    return render_template("dashboard.html", user=user)

@app.route("/login", methods=["POST"])
def login():
    email = request.form['email']
    password = request.form['password']

    data = {
        'email': email,
        'password': password
    }

    user = User.login(data)

    if user:
        session['user_id'] = user.id
        session['is_logged'] = True
        return redirect('/dashboard')
    else:
        return redirect('/log_and_reg')
    

@app.route("/logout", methods=["POST"])
def logout():
    session.clear()
    return redirect("/")