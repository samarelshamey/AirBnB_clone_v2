#!/usr/bin/python3
"""script that starts a Flask web application"""
from flask import Flask, render_template
from models import *
from models import storage


app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    """state list"""
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda state: state.name)
    return render_template('7-states_list.html', state=sorted_states)


@app.teardown_appcontext
def teardown_session(exception):
    """teardown session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
