from sqlalchemy.orm import Session
from domain.models.user import User
from domain.repositories.user_repository import UserRepository
from adapters.persistence.db_models import UserDB

class UserDAO(UserRepository):
    def __init__(self, db_session: Session):
        self.session = db_session

    def get_user_by_email(self, email: str) -> User:
        user_row = self.session.query(UserDB).filter_by(email=email).first()
        if user_row:
            return User(
                id=user_row.id,
                name=user_row.name,
                email=user_row.email,
                password=user_row.password
            )
        return None

    def save_user(self, user: User) -> None:
        new_user = UserDB(
            name=user.name,
            email=user.email,
            password=user.password
        )
        self.session.add(new_user)
        self.session.commit()
