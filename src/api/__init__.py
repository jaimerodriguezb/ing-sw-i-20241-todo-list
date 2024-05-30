from flask import Flask
from flask_restx import Api
from flask_cors import CORS
from .activity import register_routes

def create_app():
    app = Flask(__name__)
    CORS(app)  # Enable CORS for all routes and origins
    api = Api(app, title="Calendario", version="0.1.0")
    register_routes(api)

    return app