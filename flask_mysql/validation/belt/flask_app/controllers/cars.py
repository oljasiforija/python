from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.cars_model import Car
from flask_app.models.login_model import User

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        flash('Please log in')
        return redirect('/')
    
    cars = Car.cars_n_users()
    return render_template('dashboard.html', cars = cars)

@app.route('/dashboard/new')
def cars_new():
    if 'user_id' not in session:
        flash('Please log in')
        return redirect('/')
    return render_template('new_car.html')
@app.route('/dashboard/create', methods = ['POST'])
def car_create():
    if Car.validate_car(request.form):
        data = {
            'price':request.form['price'],
            'model':request.form['model'],
            'make':request.form['make'],
            'year':request.form['year'],
            'description':request.form['description'],
            'user_id': session['user_id']
        }
        Car.new_car(data)
        return redirect ('/dashboard')
    return redirect('/dashboard/new')

@app.route('/dashboard/<int:id>')
def view_car(id):
    if 'user_id' not in session:
        flash('Please log in')
        return redirect('/')
    data ={
        'id':id
    }
    car = Car.get_car_by_id(data)
    cars = Car.cars_n_users_by_id(data)
    return render_template('view_car.html', car = car, cars = cars)

@app.route('/dashboard/<int:id>/edit')
def edit_car(id):
    if 'user_id' not in session:
        flash('Please log in')
        return redirect('/')
    data ={
        'id':id
    }
    car = Car.get_car_by_id(data)
    return render_template('/edit_car.html', car = car)

@app.route('/dashboard/<int:id>/update', methods= ['POST'])
def update_car(id):
    if 'user_id' not in session:
        flash('Please log in')
        return redirect('/')
    if Car.validate_car(request.form):
        data = {
            'id':id,
            'price':request.form['price'],
            'model':request.form['model'],
            'make':request.form['make'],
            'year':request.form['year'],
            'description':request.form['description'],
            'user_id': session['user_id']
        }
        Car.car_update(data)
    return redirect('/dashboard') 

@app.route('/dashboard/<int:id>/delete')
def delete_car(id):
    if 'user_id' not in session:
        flash('Please log in')
        return redirect('/')
    data ={
        'id':id
    }
    Car.car_delete(data)
    return redirect('/dashboard')
