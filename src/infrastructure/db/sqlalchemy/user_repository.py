from typing import List, Optional

from sqlalchemy.orm import Query, Session

from ....domain.entities.user import User
from ....domain.user_repository import UserRepository


class SQLAlchemyUserRepository(UserRepository):
    """
    Secondary adapter providing ORM SQLAlchemy implementation for :class:`User`
    instances storage
    """

    def __init__(self, session: Session):
        self.session = session

    @property
    def queryset(self) -> Query:
        return self.session.query(User)

    def get(self, user_id: int) -> Optional[User]:
        return self.queryset.get(user_id)

    def all(self) -> List[User]:
        return self.queryset.all()

    def add(self, user: User) -> None:
        self.session.add(user)
        self.session.flush()
