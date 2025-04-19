from flask import Flask
from .config import config_by_name
from neomodel import config as neomodel_config


def create_app(config_name='development'):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    neomodel_config.DATABASE_URL = app.config['DATABASE_URL']

    return app
