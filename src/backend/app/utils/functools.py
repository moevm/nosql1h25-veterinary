from functools import wraps
from flask import jsonify
from neomodel import DoesNotExist

def error_handler(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            return jsonify({"error": str(e)}), 400
        except Exception as e:
            return jsonify({"error": "Internal Server Error: " + str(e)}), 500
    return wrapper


def is_entity_exists(get_func):
    """Декоратор для проверки существования сущности в базе данных."""
    def wrapper(*args, **kwargs):
        try:
            return get_func(*args, **kwargs)
        except DoesNotExist:
            return None
    return wrapper
