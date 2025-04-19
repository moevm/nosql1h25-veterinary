from flask import Flask
from .config import config_by_name


def create_app(config_name='development'):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])

    return app
