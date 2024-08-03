#!/usr/bin/python3
"""
script to start a web flask
"""
from flask import Flask, render_template
from models import storage
import sys


app = Flask(__name__)


@app.teardown_appcontext
def teardown(exception):
    """
    manages breakages
    """
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """
    routes to filter page
    """
    st = storage.all('State').values()
    am = storage.all('Amenity').values()
    return render_template('10-hbnb_filters.html', st=states, am=amenities)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
