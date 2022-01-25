#!/usr/bin/env python3
"""setup a basic Flask app"""
from flask import Flask, render_template, request, g
from flask_babel import Babel
app = Flask(__name__)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    """language configuration"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object("6-app.Config")
babel = Babel(app)


@babel.localeselector
def get_locale():
    """language best match"""
    if request.args.get('locale') in Config.LANGUAGES:
        return request.args.get('locale')
    if hasattr(g, "user"):
        if g.user.get('locale') in Config.LANGUAGES:
            return g.user.get('locale')
    return request.accept_languages.best_match(Config.LANGUAGES)


@app.route('/')
def index():
    """render html template"""
    return render_template('6-index.html')


def get_user():
    """get user"""
    userID = request.args.get('login_as')
    if userID:
        if int(userID) in users.keys():
            return users.get(int(userID))
    return None


@app.before_request
def before_request():
    """set global variable"""
    if get_user():
        g.user = get_user()


if __name__ == "__main__":
    app.run(debug=True)
