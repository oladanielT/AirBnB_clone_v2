#!/usr/bin/python3
"""
script that starts a Flask web application
"""

from flask import Flask, render_template
from models import storage
import sys
print(sys.path)


app = Flask(__name__)

@app.teardown_appcontext
def teardown(exception):
    """
    manage shutdown
    """
    storage.close()

@app.route('/states_list', strict_slashes=False)
def states_list():
    """
    routes to state
    """
    states = storage.all('States')
    return render_template('7-states_list.html', states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
