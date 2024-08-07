#!/usr/bin/python3
"""
Python script to start a flask
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_bnb():
    """
    function to return a path to /
    """
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
