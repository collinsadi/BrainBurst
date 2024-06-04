#!/usr/bin/python3
"""Tests for the user routes"""
import pytest
from app.__init__ import create_app
from flask import json

@pytest.fixture
def client():
    """initiates a client connection"""
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_fetch_users(client):
    """Tests for overall users acquisition"""
    response = client.get('/users')
    assert response.status_code == 200

def test_add_user(client):
    """Tests for creation and addition of a new user"""
    new_user = {
        "username": "testuser",
        "email": "testuser@example.com",
    }
    response = client.post('/users', data=json.dumps(new_user), content_type='application/json')
    assert response.status_code == 201
