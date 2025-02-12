#!/usr/bin/python3
""" Python script that starts a Flask web application """
from flask import Flask, abort
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """ Print Hello HBNB"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Print HBNB"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """ Print C and text"""
    return 'C {}'.format(text.replace("_", " "))


@app.route('/python', strict_slashes=False)
def python_default():
    """ Print Python is cool """
    return 'Python is cool'


@app.route('/python/<text>', strict_slashes=False)
def python(text):
    """ Print Python """
    return 'Python {}'.format(text.replace("_", " "))


@app.route('/number/<n>', strict_slashes=False)
def num(n):
    """ Print number or redirect to 404 error """
    if(n.isnumeric()):
        return '{} is a number'.format(n)
    abort(404)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
