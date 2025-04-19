from flask import Blueprint, request, jsonify
from app.services.auth_service import login_user, get_user_data, register_user
from app.utils.functools import error_handler

user_routes = Blueprint('user_routes', __name__)

@user_routes.route('/login', methods=['POST'])
@error_handler
def login():
    data = request.get_json()
    user = login_user(data)
    return jsonify({"message": "Login successful", "role": user.role}), 200

@user_routes.route('/register', methods=['POST'])
@error_handler
def register():
    data = request.get_json()
    user = register_user(data)
    return jsonify({"message": "User registered successfully"}), 201


@user_routes.route("/user", methods=['GET'])
@error_handler
def get_user():
    data = request.get_json()
    user_id = data['id']
    return get_user_data(user_id)
