#!/usr/bin/env python3
"""setup a basic Flask app"""
from flask import Flask, render_template
from flask_babel import Babel
app = Flask(__name__)


class config:
    """language configuration"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object("1-app.Config")
babel = Babel(app)


@app.route('/')
def index():
    """render html template"""
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run(debug=True)
