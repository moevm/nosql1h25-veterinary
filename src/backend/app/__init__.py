from flask import Flask
from neomodel import config as neomodel_config
from .config import config_by_name
from .api.user_routes import user_routes


def register_routes(app):
    app.register_blueprint(user_routes, url_prefix='/api/users')

def create_app(config_name='development'):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    neomodel_config.DATABASE_URL = app.config['DATABASE_URL']
    register_routes(app)
    return app
