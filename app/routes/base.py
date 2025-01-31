from flask import Blueprint, render_template

base_route = Blueprint('base_route', __name__)

@base_route.route('/connexion')
def home():
    return render_template('index.html')