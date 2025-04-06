from flask import Flask
from dotenv import load_dotenv
from adapters.persistence.db import init_db, SessionLocal
from adapters.persistence.user_dao import UserDAO
from app.use_cases.login_user import LoginUserUseCase
from app.use_cases.register_user import RegisterUserUseCase
from adapters.flask.routes import create_routes

# Cargar variables del .env
load_dotenv()

# Inicializar la app Flask
app = Flask(__name__)

# Inicializar base de datos y crear tablas si no existen
init_db()

# Crear sesión de BD e inyectar DAO
db_session = SessionLocal()
user_repo = UserDAO(db_session)

# Casos de uso
login_use_case = LoginUserUseCase(user_repo)
register_use_case = RegisterUserUseCase(user_repo)

# Registrar blueprint con rutas
app.register_blueprint(create_routes(login_use_case, register_use_case))

if __name__ == "__main__":
    app.run(debug=True)
