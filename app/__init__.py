from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    app.config.from_pyfile('../instance/config.py')

    db.init_app(app)
    api = Api(app)

    from .routes.resume_routes import ResumeUploadAPI
    api.add_resource(ResumeUploadAPI, '/api/resumes')

    return app
