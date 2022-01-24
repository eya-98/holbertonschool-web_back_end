#!/usr/bin/env python3
"""setup a basic Flask app"""
from flask import Flask, render_template
from flask_babel import Babel
app = Flask(__name__)
babel = Babel(app)


class config:
    """language configuration"""
    LANGUAGES = ["en", "fr"]
    @babel.localeselector
    def get_locale():
        return 'en'

    @babel.timezoneselector
    def get_timezone():
        return 'UTC'

@app.route('/')
def index():
    """render html template"""
    return render_template('1-index.html')

if __name__ == "__main__":
    app.run(debug=True)
