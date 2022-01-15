#!/usr/bin/env python3
""" Module of Users views
"""
from api.v1.views import app_views
from flask import abort, jsonify, request
from models.user import User
from api.v1.auth.auth import Auth
from os import getenv


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def session_auth() -> str:
    """create a session"""
    email = request.form.get("email", None)
    password = request.form.get("password", None)
    if email is None or email == "":
        return jsonify({"error": "email missing"}), 400
    if password is None or password == "":
        return jsonify({"error": "password missing"}), 400
    user = User.search({"email": email})
    if user is None or len(user) == 0:
        return jsonify({"error": "no user found for this email"}), 404
    if user[0].is_valid_password(password) is None:
        return jsonify({"error": "wrong password"}), 401
    else:
        from api.v1.app import auth
        sessionId = auth.create_session(user[0].id)
        cookie_name = getenv('SESSION_NAME')
        session = jsonify(user[0].to_json())
        session.set_cookie(cookie_name, sessionId)
        return session
