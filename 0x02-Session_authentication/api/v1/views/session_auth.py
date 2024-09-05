#!/usr/bin/env python3
""" Module of Session Auth views
"""
from os import getenv
from flask import jsonify, abort, request
from api.v1.views import app_views
from models.user import User


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login():
    """POST /api/v1/auth_session/login"""
    email = request.form.get("email")
    password = request.form.get("password")
    if email is None or email == "":
        return jsonify({"error": "email missing"}), 400
    if password is None or password == "":
        return jsonify({"error": "password missing"}), 400
    users = User.search({"email": email})
    if users is None or users == []:
        return jsonify({"error": "no user found for this email"}), 404
    from api.v1.app import auth
    for user in users:
        if user.is_valid_password(password):
            return jsonify({"error": "wrong password"}), 401
        sessionID = auth.create_session(user.id)
        json = jsonify(user.to_json())
        json.set_cookie(getenv("SESSION_NAME"), sessionID)
        return json


@app_views.route('/auth_session/logout',
                 methods=['DELETE '], strict_slashes=False)
def logout():
    """DELETE /api/v1/auth_session/logout"""
    from api.v1.app import auth
    if auth.destroy_session():
        return jsonify({}), 200
    abort(404)
