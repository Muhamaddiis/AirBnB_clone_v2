#!/usr/bin/python3
from flask import Flask

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def hello_world():
    """return hello HBNB"""
    return "Hello HBNB!"

@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """return HBNB"""
    return "HBNB"

@app.route("/c/<text>", strict_slashes=False)
def c_is_fun(text):
    """return text given"""
    return "C {}".format(text.replace("_", " "))

@app.route("/python/", defaults={'text': 'is cool'})
@app.route("/python/<text>", strict_slashes=False)
def python_is_cool(text):
    """display “Python ”, followed by the value of the text"""
    return "python {}".format(text.replace("_", " "))

@app.route("/number/<int:n>", strict_slashes=False)
def is_number(n):
    """display “n is a number” only"""
    return "{} is a number".format(n)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
