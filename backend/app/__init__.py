#!/usr/bin/python3
"""
This module initiates the Flask application
and the database connection.
"""
from flask import Flask
from app.config import Config
#from flask_pymongo import PyMongo
from flask_cors import CORS

mongo = PyMongo()

def create_app():
    """Initiates the Flask application"""
    app = Flask(__name__)
    app.config.from_object(Config)
    mongo.init_app(app)
    CORS(app)

    with app.app_context():
        from app.routes import quiz_routes, user_routes
        app.register_blueprint(quiz_routes.bp)
        app.register_blueprint(user_routes.bp)

    return app
