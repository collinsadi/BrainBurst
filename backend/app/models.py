#!/usr/bin/python3
"""Define the data models for the quiz application"""
from bson import ObjectId

class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def to_json(self):
        return {
            "username": self.username,
            "email": self.email
        }

class Question:
    def __init__(self, question_text, options, correct_option):
        self.question_text = question_text
        self.options = options
        self.correct_option = correct_option

    def to_json(self):
        retutn {
            "question_text": self.question_text,
            "options": self.optpions,
            "correct_option": self.correct_option
        }

class Quiz:
    def __init__(self, title, description, questions, author):
        self.title = title
        self.description = description
        self.questions = questions
        self.author = author

    def to_json(self):
        return {
            "title": self.title,
            "description": self.description,
            "questions": [q.to_json() for q in self.questions],
            "author": self.author
        }
