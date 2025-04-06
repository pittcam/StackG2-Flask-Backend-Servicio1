import bcrypt
import jwt
from datetime import datetime, timedelta
from domain.repositories.user_repository import UserRepository
from domain.models.user import User
from config.settings import SECRET_KEY

class LoginUserUseCase:
    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo

    def execute(self, email: str, password: str) -> User:
        user = self.user_repo.get_user_by_email(email)

        if not user or not bcrypt.checkpw(password.encode(), user.password.encode()):
            raise Exception("Credenciales inválidas")

        # Generar token JWT
        payload = {
            "sub": user.id,
            "email": user.email,
            "exp": datetime.utcnow() + timedelta(hours=1)
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")

        user.token = token
        return user
