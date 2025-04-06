from abc import ABC, abstractmethod
from domain.models.user import User

class UserRepository(ABC):

    @abstractmethod
    def get_user_by_email(self, email: str) -> User:
        pass

    @abstractmethod
    def save_user(self, user: User) -> None:
        pass
