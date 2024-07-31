#!/usr/bin/python3
"""
script to start a web flask
"""
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_bnb():
    """route to hello_bnb"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def show_hbnb():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def show_c(text):
    text = text.replace('_', ' ')
    return f"C {text}"

@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def show_python(text='is cool'):
    text = text.replace('_', ' ')
    return f"Python {text}"


@app.route('/number/<int:n>', strict_slashes=False)
def show_num(n):
    return f"{n} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def show_templates(n):
    return render_template('5-number.html', Number=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
