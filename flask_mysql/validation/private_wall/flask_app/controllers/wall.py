from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.wall_model import Message


@app.route('/wall')
def index_wall():
    return render_template('wall.html')