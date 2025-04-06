import os

# Carga de configuración desde variables de entorno
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://user:password@localhost:5432/mi_base_de_datos"
)

SECRET_KEY = os.getenv(
    "SECRET_KEY",
    "clave-secreta-default"
)

# Configuración extra (si usás SQLAlchemy dentro de Flask directamente)
SQLALCHEMY_DATABASE_URI = DATABASE_URL
SQLALCHEMY_TRACK_MODIFICATIONS = False
