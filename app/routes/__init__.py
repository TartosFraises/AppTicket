# routes/__init__.py
from flask import Blueprint
from .base import base_route

def init_routes(app):
    # Enregistrement des blueprints
    app.register_blueprint(base_route)