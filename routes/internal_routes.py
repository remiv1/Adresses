from flask import render_template, Blueprint
from __init__ import app

internal_routes = Blueprint('internal_routes', __name__)

@internal_routes.route('/')
def home():
    return render_template('index.html')

@internal_routes.route('/adresse')
def adresse():
    # Logic for address search goes here
    return render_template('adresse.html')