#!/usr/bin/python3
"""Populates the database of the app"""
from app import create_app
from app.services.quiz_service import create_quiz
from app.services.user_service import create_user

app = create_app()
with app.app_context():
    #make samples
    sample_quiz = {
        "title": "Sample Quiz",
        "description": "This is a sample",
        "questions": [
            {
                "text": "What is the capital of France?",
                "options": ["Paris", "London", "Berlin", "Kigali"]
                "correct_option": "Paris"
            }
        ],
        "author": "Admin"
    }
    create_quiz(sample_quiz)

    #Add sample users
    sample_user = {
        "username": "admin",
        "email": "admin@example.com"
    }
    create_user(sample_user)
