from flask import Flask, render_template, Blueprint, redirect, url_for
from routes.internal_routes import internal_routes
from routes.external_routes import external_routes
from __init__ import app

# Register blueprints for internal and external routes
app.register_blueprint(internal_routes, url_prefix='/internal')
app.register_blueprint(external_routes, url_prefix='/external')

@app.route('/')
def index():
    return redirect(url_for('internal_routes.home'))

if __name__ == '__main__':
    app.run(debug=True)