from flask import Flask
from .routes.__init__ import init_routes

def create_app():
    app = Flask(__name__)
    
    init_routes(app)
    return app