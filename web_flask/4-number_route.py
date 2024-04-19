#!/usr/bin/python3
from flask import Flask

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def helloWorld():
    return "Hello HBNB!"

@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"

@app.route("/c/<text>", strict_slashes=False)
def c_is_fun(text):
    return "C {}".format(text.replace("_", " "))

@app.route("/python/", defaults={'text': 'is cool'})
@app.route("/python/<text>", strict_slashes=False)
def python_is_cool(text):
    return "python {}".format(text.replace("_", " "))

@app.route("/number/<int:n>", strict_slashes=False)
def isnumber(n):
    return "{} is a number".format(n)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)