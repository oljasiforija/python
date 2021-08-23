from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.paintings_model import Painting
from flask_app.models.login_model import User

@app.route('/paintings')
def paintings():
    if 'user_id' not in session:
        flash('Please log in')
        return redirect('/')
    paintings = Painting.get_paintings()
    return render_template('paintings.html', paintings = paintings)

@app.route('/paintings/new')
def paintings_new():
    if 'user_id' not in session:
        flash('Please log in')
        return redirect('/')
    return render_template('new_painting.html')

@app.route('/paintings/create', methods = ['POST'])
def paintings_create():
    if Painting.validate_painting(request.form):
        data = {
            'title':request.form['title'],
            'description':request.form['description'],
            'price':request.form['price'],
            'user_id':session['user_id']
        }
        Painting.create_painting(data)
        flash('You added a painting!')
        return redirect('/paintings')
    return redirect('/paintings/new')

@app.route('/paintings/<int:id_painting>')
def view_painting(id_painting):
    if 'user_id' not in session:
        flash('Please log in')
        return redirect('/')
    data = {
        'id_painting':id_painting
    }
    paintings = Painting.get_painting_by_id(data)
    return render_template('view_painting.html', paintings = paintings)

@app.route('/paintings/<int:id_painting>/edit')
def edit_painting(id_painting):
    if 'user_id' not in session:
        flash('Please log in')
        return redirect('/')
    data = {
        'id_painting':id_painting
    }
    paintings = Painting.get_painting_by_id(data)
    return render_template('edit_painting.html', paintings = paintings)

@app.route('/paintings/<int:id_painting>/update', methods= ['POST'])
def update_painting(id_painting):
    if 'user_id' not in session:
        flash('Please log in')
        return redirect('/')
    if Painting.validate_painting(request.form):
        data = {
            'id_painting':id_painting,
            'title':request.form['title'],
            'description':request.form['description'],
            'price':request.form['price'],
            'user_id':session['user_id']
        }
        Painting.update_painting(data)
    return redirect('/paintings')
    

@app.route('/paintings/<int:id_painting>/delete')
def delete_painting(id_painting):
    if 'user_id' not in session:
        flash('Please log in')
        return redirect('/')
    data = {
        'id_painting':id_painting
    }
    Painting.delete_painting(data)
    return redirect ('/paintings')

    
