#!/usr/bin/python3
"""Tests for the quiz routes"""
import pytest
from app.__init__ import create_app
from flask import json

@pytest.fixture
def client():
    """initiates the client"""
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_fetch_quizzes(client):
    """Tests for fetching overall quizzes"""
    response = client.get('/quizzes')
    assert response.status_code == 200

def test_add_quiz(client):
    """Tests for adding and creating a new quiz"""
    new_quiz = {
        "title": "Sample Quiz",
        "description": "This is a sample",
        "questions": [],
        "author": "Author"
    }
    response = client.post('/quizzes', data=json.dumps(new_quiz), content_type='application/json')
    assert response.status_code == 201
