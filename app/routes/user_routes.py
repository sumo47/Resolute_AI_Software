from flask import Blueprint, request, jsonify
from app.models import User
from app.crud import create_user, get_user_by_email, update_user, delete_user
from app.auth.jwt_handler import token_required

user_bp = Blueprint('user_bp', __name__)

# Route to create a user (already implemented)
@user_bp.route("/create", methods=["POST"])
def create_user_route():
    data = request.get_json()
    user = create_user(data)
    if user:
        return jsonify({"message": "User created successfully", "user": user}), 201
    return jsonify({"message": "Failed to create user"}), 400

# Route to get user by email
@user_bp.route("/<email>", methods=["GET"])
@token_required
def get_user(email):
    user = get_user_by_email(email)
    if user:
        return jsonify({"user": user}), 200
    return jsonify({"message": "User not found"}), 404

# Route to update user
@user_bp.route("/<email>", methods=["PUT"])
@token_required
def update_user_route(email):
    data = request.get_json()
    user = update_user(email, data)
    if user:
        return jsonify({"message": "User updated successfully", "user": user}), 200
    return jsonify({"message": "User not found or failed to update"}), 404

# Route to delete user
@user_bp.route("/<email>", methods=["DELETE"])
@token_required
def delete_user_route(email):
    result = delete_user(email)
    if result:
        return jsonify({"message": "User deleted successfully"}), 200
    return jsonify({"message": "User not found or failed to delete"}), 404
