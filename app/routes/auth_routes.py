from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from app.crud import get_user_by_email, create_user
from app.auth.jwt_handler import create_jwt_token
from app.models import UserSchema, TokenSchema

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    email = data.get("email")
    password = data.get("password")

    db_user = get_user_by_email(email)
    if not db_user or not check_password_hash(db_user['hashed_password'], password):
        return jsonify({"error": "Invalid credentials"}), 401

    token = create_jwt_token({"sub": email})
    return jsonify({"access_token": token, "token_type": "bearer"})

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.json
    email = data.get("email")
    username = data.get("username")
    password = data.get("password")

    if get_user_by_email(email):
        return jsonify({"error": "Email already registered"}), 400

    create_user(email, username, password)
    return jsonify({"message": "User registered successfully"}), 201
