import bcrypt
from domain.models.user import User
from domain.repositories.user_repository import UserRepository

class RegisterUserUseCase:
    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo

    def execute(self, name: str, email: str, password: str) -> None:
        # Verificar si el usuario ya existe
        existing_user = self.user_repo.get_user_by_email(email)
        if existing_user:
            raise Exception("El usuario ya existe")

        # Hashear la contraseña
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        # Crear objeto de dominio
        new_user = User(
            id=None,
            name=name,
            email=email,
            password=hashed_password.decode('utf-8'),
            token=None
        )

        # Guardar usuario
        self.user_repo.save_user(new_user)
