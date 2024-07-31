#!/usr/bin/env python3
"""A basic Flask app"""

from flask import Flask, render_template, request, g
from flask_babel import Babel, gettext as _


class Config:
    """Configuration class for Flask-Babel. Support two languages:
    - English
    - Fensh
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
    """This function Use get_user function to find a user if any, and
    set it as global on flask.g.user"""
    g.user = get_user()


def get_user():
    """returns a user dictionary or None if the ID cannot be found
    """
    user_id = request.args.get('login_as')
    if user_id:
        return users.get(int(user_id))
    return None


@babel.localeselector
def get_locale() -> str:
    """Determine the best match with our supported languages
    """
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale

    if g.user:
        locale = g.user.get('locale')
        if locale and locale in app.config['LANGUAGES']:
            return locale

    locale = request.headers.get('locale', None)
    if locale in app.config['LANGUAGES']:
        return locale

    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index() -> str:
    """Renders the template
    """
    return render_template('6-index.html')


if __name__ == '__main__':
    app.run()
