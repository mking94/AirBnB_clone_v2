#!/usr/bin/python3
""" Python script that starts a Flask web application """
from flask import Flask
app = Flask(__name__)
@app.index('/')
def index():
    app.url_map.strict_slashes = False
    return 'Hello HBNB!'

if __name__ == '__main__':
      app.run(host="0.0.0.0", port=5000, debug=True)
