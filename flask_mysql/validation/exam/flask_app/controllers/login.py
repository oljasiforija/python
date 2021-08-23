from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.login_model import User
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods = ['POST'])
def login_user():
    users = User.get_user(request.form)
    if not users:
        flash ('Email is incorrect.')
        return redirect ('/')
    if not bcrypt.check_password_hash(users.password, request.form['password']):
        flash('Password is incorrect.')
        return redirect('/')
    session['user_id'] = users.id
    session['first_name'] = users.first_name
    return redirect('/paintings')

@app.route('/success_login')
def success_login():
    if 'user_id' not in session:
        flash ('Please log in')
        return redirect('/')

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

@app.route('/register', methods = ['POST'])
def register():
    if User.validate_user(request.form):
        pw_hash = bcrypt.generate_password_hash(request.form['password'])
        data = {
            'first_name':request.form['first_name'],
            'last_name':request.form['last_name'],
            'email':request.form['email'],
            'password':pw_hash
        }
        User.add_user(data)
        flash('You can log in.')
    return redirect('/')

