#!/usr/bin/python3
"""
script to start a web flask
"""

from flask import Flask


app = Flask(__name__)
@app.route('/', strict_slashes=False)
def hello_bnb():
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def show_hbnb():
    return "HBNB"



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
