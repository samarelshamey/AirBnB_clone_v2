#!/usr/bin/python3
"""script that starts a Flask web application"""
from flask import Flask, render_template
from models import *
from models import storage
app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    """state list"""
    state = sorted(list(storage.all("State").values()), key=lambda x: x.name)
    return render_template('7-states_list.html', state=state)


@app.teardown_appcontext
def teardown_session(exception):
    """teardown session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
