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
    return render_template('3-index.html')


if __name__ == "__main__":
    app.run(debug=True)
