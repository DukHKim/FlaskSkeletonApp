# -*- coding: utf-8 -*-
"""
    Flask Skeleton app
    ~~~~~~~~~~~~~~~~~

    Use this for a basic Flask app setup.
"""

import os
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash


# create our little application :)
app = Flask(__name__)

# Load default config and override config from an environment variable
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'flaskr.db'),
    DEBUG=True,
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)


# Helpful

#@app.cli.command('initdb')
#@app.teardown_appcontext

# Homepage route

@app.route('/')
def home():
    return render_template('home.html')
# Possible decorators for functions

#@app.route('/add', methods=['POST'])
#@app.route('/login', methods=['GET', 'POST'])
#@app.route('/logout')
