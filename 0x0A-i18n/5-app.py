#!/usr/bin/env python3
"""setup a basic Flask app"""
from flask import Flask, render_template, request
from flask_babel import Babel
app = Flask(__name__)


class Config:
    """language configuration"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object("3-app.Config")
babel = Babel(app)


@babel.localeselector
def get_locale():
    """language best match"""
    if request.args.get('locale') in Config.LANGUAGES:
        return request.args.get('locale')
    return request.accept_languages.best_match(
       Config.LANGUAGES)


@app.route('/')
def index():
    """render html template"""
    return render_template('5-index.html')


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

def get_user():
    """get user"""
    userID = request.args.get('login_as')
    if userID in users.keys()
        return users.get(int(userID)):
    return None

@app.before_request
def before_request():
    """set a global object""""
    if get_user():
        g.user = get_user()


if __name__ == "__main__":
    app.run(debug=True)
