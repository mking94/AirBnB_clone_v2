#!/usr/bin/python3
""" Python script that starts a Flask web application """
from flask import Flask, abort, render_template
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


@app.route('/number_template/<n>', strict_slashes=False)
def num_temp(n):
    """ Print number in html code
    or redirect to 404 error """
    if(n.isnumeric()):
        return render_template("5-number.html", value=n)
    abort(404)


@app.route('/number_odd_or_even/<n>', strict_slashes=False)
def num_type(n):
    """ Print number odd or even in html code
    or redirect to 404 error """
    if(n.isnumeric()):
        if(int(n) % 2 == 0):
            param = '{} is even'.format(n)
            return render_template("6-number_odd_or_even.html", value=param)
        else:
            param = '{} is odd'.format(n)
            return render_template("6-number_odd_or_even.html", value=param)
    abort(404)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
