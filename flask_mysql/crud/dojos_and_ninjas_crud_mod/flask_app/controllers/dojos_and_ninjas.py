from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.dojos import Dojos
from flask_app.models.ninjas import Ninjas

@app.route('/')
def index():
    return 'Welcome'

@app.route('/dojos')
def all_dojos():
    dojos = Dojos.get_all()
    print (dojos)
    return render_template('dojos.html',  dojos = dojos)

@app.route('/dojos/add_dojo', methods = ["POST"])
def add_dojo():
    data = { 
        'name': request.form['add_dojo']
        }
    Dojos.add_dojo(data)
    return redirect ('/dojos')

@app.route('/ninjas')
def ninja():
    dojos = Dojos.get_all()
    return render_template('ninjas.html', dojos = dojos, ninja = ninja)


@app.route('/add_ninja', methods = ["POST"])
def add_ninja():
    data = {
        'dojo_id':request.form['dojo_id'],
        'first_name':request.form["first_name"],
        'last_name':request.form["last_name"],
        'age':request.form["age"]
    }
    print(data)
    Ninjas.add_ninja(data)
    return redirect('/dojos')

@app.route('/dojos/<int:dojo_id>')
def single_dojo(dojo_id):
    data = {
        'dojo_id': dojo_id
    }
    return render_template('dojo.html', dojo = Dojos.single_dojo(data))


