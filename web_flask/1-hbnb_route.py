#!/usr/bin/python3
""" Python script that starts a Flask web application """
from flask import Flask
app = Flask(__name__)
@app.route('/',strict_slashes = False)
def index():
    """ Print Hello HBNB"""
    return 'Hello HBNB!'

@app.hbnb('/hbnb',strict_slashes = False)
def hbnb():
    """ Print HBNB"""
    return 'HBNB'

if __name__ == '__main__':
      app.run(host="0.0.0.0", port=5000)