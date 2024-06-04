#!/usr/bin/python3
"""Handles the routes of the users"""
from flask import Blueprint, request, jsonify
from app.services.user_service import create_user, get_all_users,

bp = Blueprint('user', __name__)

@bp.route('/users', methods=['GET'])
def fetch_users():
    """Gets the overall users info"""
    users = get_all_users()
    return jsonify(users), 200

@bp.route('/user/<user_id>', methods=['GET'])
def fetch_user(user_id):
    """Gets the user info by their id"""
    user = get_user_by_id(user_id)
    if user:
        return jsonify(user), 200
    return jsonify({"error": "User not found"}), 404

@bp.route('/users' methods=['POST'])
def add_user():
    """adds a new users' info"""
    data = request.json
    user = create_user(data)
    return jsonify(user.to_json()), 201
