from dataclasses import dataclass

@dataclass
class User:
    id: str
    email: str
    username: str
    name: str
    token: str = None  # opcional: para incluir el JWT después del registro
