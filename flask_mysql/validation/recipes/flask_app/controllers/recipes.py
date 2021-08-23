from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.recipes_model import Recipe



@app.route('/dashboard')
def dashboard():
    recipes = Recipe.get_recipe()
    print(recipes)
    return render_template ('dashboard.html', recipes = recipes)

@app.route('/recipes/new')
def recipes():
    if 'user_id' not in session:
        flash('Please log in')
        return redirect('/')
    return render_template('recipe.html')

@app.route('/recipes/create', methods= ['POST'])
def create_recipe():
    if Recipe.validate_recipe(request.form):
        data = {
            'name':request.form['name'],
            'description':request.form['description'],
            'instructions':request.form['instructions'],
            'date':request.form['date'],
            'under_30_min':request.form['under_30_min'],
            'user_id': session['user_id']
        }
        Recipe.create_recipe(data)
        flash('You created a recipe!')
    return redirect('/dashboard')

@app.route('/recipes/<int:id_recipes>')
def view_recipe(id_recipes):
    if 'user_id' not in session:
        flash('Please log in')
        return redirect('/')
    data = {
        'id_recipes':id_recipes
    }
    recipes = Recipe.get_recipes_by_id(data)
    return render_template('view_recipe.html', recipes = recipes)

@app.route('/recipes/<int:id_recipes>/edit')
def edit_recipe(id_recipes):
    if 'user_id' not in session:
        flash('Please log in')
        return redirect('/')
    data = {
        'id_recipes':id_recipes
    }
    recipes = Recipe.get_recipes_by_id(data)
    return render_template('edit_recipe.html', recipes = recipes)

@app.route('/recipes/<int:id_recipes>/update', methods = ['POST'])
def update_recipe(id_recipes):
    if 'user_id' not in session:
        flash('Please log in')
        return redirect('/')
    if Recipe.validate_recipe(request.form):
        data = {
            'id_recipes':id_recipes,
            'name':request.form['name'],
            'description':request.form['description'],
            'instructions':request.form['instructions'],
            'date':request.form['date'],
            'under_30_min':request.form['under_30_min']
        }
        Recipe.update_recipe(data)
    return redirect('/dashboard')

@app.route('/recipes/<int:id_recipes>/delete')
def delete(id_recipes):
    if 'user_id' not in session:
        flash('Please log in')
        return redirect('/')
    data = {
        'id_recipes':id_recipes
        }
    Recipe.delete_recipe(data)
    return redirect('/dashboard')
