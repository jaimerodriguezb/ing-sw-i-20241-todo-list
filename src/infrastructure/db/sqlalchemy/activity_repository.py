from typing import List, Optional

from sqlalchemy.orm import Query, Session

from ....domain.entities.activity import Activity
from ....domain.activity_repository import ActivityRepository


class SQLAlchemyActivityRepository(ActivityRepository):
    """
    Secondary adapter providing ORM SQLAlchemy implementation for :class:`Activity`
    instances storage
    """

    def __init__(self, session: Session):
        self.session = session

    @property
    def queryset(self) -> Query:
        return self.session.query(Activity)

    def get(self, acti_id: int) -> Optional[Activity]:
        return self.queryset.get(acti_id)

    def all(self) -> List[Activity]:
        return self.queryset.all()

    def add(self, activity: Activity) -> None:
        self.session.add(activity)
        self.session.flush()
