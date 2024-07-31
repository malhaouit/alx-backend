#!/usr/bin/env python3
"""Flask app"""

from flask import Flask, render_template, request, g
from flask_babel import Babel, gettext as _
from typing import Optional


class Config:
    """Configuration class for Flask-Babel.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)

users = {
        1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
        2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
        3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
        4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
        }



@app.before_request
def before_request():
    g.user = get_user()


def get_user() -> Optional[dict]:
    user_id = request.args.get('login_as')
    if user_id and user_id.isdigit():
        user_id = int(user_id)
        return users.get(user_id)
    return None


@babel.localeselector
def get_locale() -> str:
    """Determine the best match with our supported languages.
    """
    user = getattr(g, 'user', None)
    if user and user.get('locale') in app.config['LANGUAGES']:
        return user['locale']
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def display_hello_world() -> str:
    """Outputs 'Welcome to Holberton' as page title and 'Hello world'
    as header.
    """
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run()
