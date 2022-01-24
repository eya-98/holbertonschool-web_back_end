#!/usr/bin/env python3
"""setup a basic Flask app"""
from urllib import request
from flask import Flask, render_template
from flask_babel import Babel
app = Flask(__name__)


class Config:
    """language configuration"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object("1-app.Config")
babel = Babel(app)

@babel.localeselector
def get_local():
    return request.accept_languages.best_match(app.config[1-app.Config.Languages])

@app.route('/')
def index():
    """render html template"""
    return render_template('2-index.html')


if __name__ == "__main__":
    app.run(debug=True)
