from flask import Flask
from app.routes.base import base_route

app = Flask(__name__, template_folder='app/templates')
app.register_blueprint(base_route)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)