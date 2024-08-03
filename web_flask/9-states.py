#!/usr/bin/python3
"""
script that starts a Flask web application
"""

from flask import Flask, render_template
from models import storage
import sys


app = Flask(__name__)


@app.teardown_appcontext
def teardown(exception):
    """
    manage shutdown
    """
    storage.close()


@app.route('/states', default={"id": 1} strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states_id(id):
    """
    routes states_id
    """
    if id == 1:
        states = storage.all('State').values()
        return render_template('9-states.html', states=states)
    else:
        for state in storage.all('State').values():
            if state.id == id:
                return render_template('9-states.html', state=state)
        return render_template('9-states.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
