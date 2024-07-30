#!/usr/bin/env python3
"""Basic Flask app."""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def display_hello_world() -> str:
    """Outputs “Welcome to Holberton” as page title and “Hello world”
    as header.
    """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run()
