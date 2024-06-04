#!/usr/bin/python3
"""Handles the overall routes in the quiz"""
from flask import Blueprint, request, jsonify
from app.services.quiz_service import create_quiz, get_all_quizzes, get_quiz_by_id

bp = Blueprint('quiz', __name__)

@bp.route('/quizzes', methods=['GET'])
def fetch_quizzes():
    """fetches the overall quizzes info"""
    quizzes = get_all_quizzes()
    return jsonify(quizzes), 200

@bp.route('/quiz/<quiz_id>', methods=['GET'])
def fetch_quiz(quiz_id):
    """fetches the single quiz info by using id"""
    quiz = get_quiz_by_id(quiz_id)
    if quiz:
        return jsonify(quiz), 200
    return jsonify({"error": "Quiz not found"}), 404

@bp.route('/quizzes', methods=['POST'])
def add_quiz():
    """creates and adds a quiz"""
    data = request.json
    quiz = create_quiz(data)
    return jsonify(quiz.to_json()), 201
