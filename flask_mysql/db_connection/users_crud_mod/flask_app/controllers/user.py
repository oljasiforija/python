from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.users import Users


@app.route('/')
def index():
    users = Users.get_all()
    print (users)
    return render_template('read_all.html', users = users)

@app.route('/create')
def create_user():
    return render_template('create.html')

@app.route('/display/<int:id>')
def display(id):
    data = { 
        'id': id}
    result = Users.get_user(data)
    return render_template('show.html', user = result)
    
@app.route('/home')
def return_home():
    return redirect ('/')

@app.route('/submit', methods = ['POST'])
def submit_user():
    data = { 
        'fname':request.form['first_name'],
        'lname':request.form['last_name'], 
        'email':request.form['email']}
    Users.save(data)
    return redirect('/')

@app.route('/edit/<int:id>')
def edit_user(id):
    data = { 
        'id': id}
    results = Users.get_user(data)
    return render_template('edit_user.html', user = results)
    

@app.route('/edit_user/<int:id1>', methods = ["POST"])
def submit_new_user(id1):
    data = {
        'id':id1,
        'fname':request.form['first_name'],
        'lname':request.form['last_name'], 
        'email':request.form['email']
    }
    Users.edit(data)
    return redirect('/')

@app.route('/delete/<int:id>')
def delete(id):
    data = { 
        'id': id}
    Users.delete(data)
    return redirect('/')