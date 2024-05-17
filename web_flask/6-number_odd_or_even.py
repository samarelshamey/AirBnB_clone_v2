#!/usr/bin/python3
"""script that starts a Flask web application"""
from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """return Hello HBNB"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """return HBNB"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """display “C ” followed by the value of the text"""
    return "C " + text.replace("_", " ")


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    """display “Python ” followed by the value of the text"""
    return "Python " + text.replace("_", " ")


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """display n if it's an integer"""
    return format(n) + " is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """display n if it's an integer"""
    return render_template('5-number.html', n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def even_or_odd(n):
    """display n s oddd or even"""
    if n % 2 == 0:
        evenn = "even"
    else:
        evenn = "odd"
    return render_template('6-number_odd_or_even.html', n=n, evenn=evenn)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
