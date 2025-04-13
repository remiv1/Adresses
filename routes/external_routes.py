from flask import Blueprint, redirect, request
import requests
from flask import render_template

external_routes = Blueprint('external_routes', __name__)

@external_routes.route('/')
def redirect_to_external():
    chemin = request.args.get('adresse')
    chemin = chemin.replace(' ', '+')
    chemin = chemin.replace('\'', '%27')
    chemin = chemin.replace('\"', '%22')
    chemin = chemin.replace('(', '%28')
    chemin = chemin.replace(')', '%29')
    chemin = chemin.replace('!', '%21')
    chemin = chemin.replace('?', '%3F')
    chemin = chemin.replace('&', '%26')
    chemin = chemin.replace('=', '%3D')
    chemin = chemin.replace(':', '%3A')
    chemin = chemin.replace(';', '%3B')
    chemin = chemin.replace('+', '%2B')
    chemin = chemin.replace(',', '%2C')
    chemin = chemin.replace('/', '%2F')
    # Send a GET request to the external URL
    response = requests.get('https://data.geopf.fr/geocodage/search?q=' + chemin)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()

        # Define the Adresse class
        class Adresse:
            def __init__(self, adresse_data):
                self.data = adresse_data

        # Create an Adresse object with the JSON data
        adresse_obj = Adresse(data)

        # Render the HTML page with the Adresse object
        return render_template('adresse.html', adresse=adresse_obj)
    else:
        # Handle the error case
        return f"Error: Unable to fetch data, status code {response.status_code}"