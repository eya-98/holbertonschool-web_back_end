#!/usr/bin/env python3
""" Module of Users views
"""
from api.v1.views import app_views
from flask import abort, jsonify, request
from models.user import User
from api.v1.auth.auth import Auth
from api.v1.auth.session_auth import SessionAuth
from os import getenv
from api.v1.app import auth

@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def session_auth() -> str:
    """create a session"""
    email = request.form.get("email", None)
    if email is None or email == "":
        return jsonify({"error": "email missing"}), 400
    password = request.form.get("password", None)
    if password is None or password == "":
        return jsonify({"error": "password missing"}), 400
    user = User.search({"email": email})
    if user is None or len(user) == 0:
        return jsonify({"error": "no user found for this email"}), 404
    if user[0].is_valid_password(password) is False:
        return jsonify({"error": "wrong password"}), 401
    from api.v1.app import auth
    sessionId = auth.create_session(user[0].id)
    cookie_name = getenv('SESSION_NAME')
    session = jsonify(user[0].to_json())
    session.set_cookie(cookie_name, sessionId)
    return session


@app_views.route('/auth_session/logout', methods=['DELETE'],
                 strict_slashes=False)
def delete_and_logout_session() -> str:
    """delete session and logout session
    """
    if auth.destroy_session(request) is False:
        return abort(404)
    auth.destroy_session(request)
    return jsonify({}), 200
# _my_session_id=91d82359-3dd0-4ff7-8702-5d014b1d542b