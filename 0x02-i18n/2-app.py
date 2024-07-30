#!/usr/bin/env python3
"""Flask app"""

from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """Configuration class for Flask-Babel.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """Determine the best match with our supported languages.
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def display_hello_world() -> str:
    """Outputs 'Welcome to Holberton' as page title and 'Hello world'
    as header.
    """
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run()
