from flask import Flask, request
from flask_cors import CORS



def create_app():
    app = Flask(__name__)
    CORS(app, resources={r"/*": {"origins": "*", "methods": ["GET", "POST"]}})
    app.config['CORS_HEADERS'] = 'Content-Type'
    app.config['SECRET_KEY']='placerHolderKey'
    
    

    from .auth import auth

    app.register_blueprint(auth,url_prefix='/')


    return app
