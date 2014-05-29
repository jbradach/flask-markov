# -*- coding: utf-8 -*-
#!/usr/bin/env python
from flask import Flask, render_template, url_for
from pymarkovchain import MarkovChain
import os

app = Flask(__name__)

mc = MarkovChain(os.path.join(app.root_path, 'sample-markov.db'))

@app.route('/')
def index():
    """
    Returns five lines from Markov chain data.
    """
    result = []
    for line in range(0, 5):
        result.append(mc.generateString())
    return render_template('index.html', result=result)

@app.errorhandler(404)
def internal_error(error):
    """
    404 error.
    """
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_error(error):
    """
    500 error.
    """
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run()
    