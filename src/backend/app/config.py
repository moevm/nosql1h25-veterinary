import os


class BaseConfig:
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.environ.get("SECRET_KEY", "devkey")

    NEO4J_HOST = os.environ.get("NEO4J_HOST", "db")
    NEO4J_PORT = os.environ.get("NEO4J_PORT", "7687")
    NEO4J_USERNAME = os.environ.get("NEO4J_USERNAME", "neo4j")
    NEO4J_PASSWORD = os.environ.get("NEO4J_PASSWORD", "password")

    DATABASE_URL = f"bolt://{NEO4J_USERNAME}:{NEO4J_PASSWORD}@{NEO4J_HOST}:{NEO4J_PORT}"


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class TestingConfig(BaseConfig):
    TESTING = True


config_by_name = {
    'development': DevelopmentConfig,
    'testing': TestingConfig
}
