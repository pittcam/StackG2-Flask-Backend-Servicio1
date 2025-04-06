from flask import Blueprint, request, jsonify
from app.use_cases.login_user import LoginUserUseCase
from app.use_cases.register_user import RegisterUserUseCase

def create_routes(login_use_case: LoginUserUseCase, register_use_case: RegisterUserUseCase):
    auth = Blueprint("auth", __name__)

    @auth.route("/login", methods=["POST"])
    def login():
        data = request.get_json()
        email = data.get("email")
        password = data.get("password")

        try:
            user = login_use_case.execute(email, password)
            return jsonify({
                "id": user.id,
                "name": user.name,
                "email": user.email,
                "token": user.token
            }), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 401

    @auth.route("/register", methods=["POST"])
    def register():
        data = request.get_json()
        name = data.get("name")
        email = data.get("email")
        password = data.get("password")

        try:
            register_use_case.execute(name, email, password)
            return jsonify({"message": "Usuario registrado correctamente"}), 201
        except Exception as e:
            return jsonify({"error": str(e)}), 400

    return auth
