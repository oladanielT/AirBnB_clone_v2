#!/usr/bin/python3
"""Python script to start a flask application"""

from flask import Flask

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def hello_bnb():
    """route to hello_bnb"""
    return "Hello HBNB!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
