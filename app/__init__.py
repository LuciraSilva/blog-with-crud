from app import views
from flask import Flask


def create_app():
    app = Flask(__name__)
    
    app.config['JSON_SORT_KEYS'] = False
    
    views.init_app(app)
    
    return app