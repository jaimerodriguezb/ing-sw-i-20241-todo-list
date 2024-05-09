from ..uow import UnitOfWork
from ...domain.activity_repository import ActivityRepository
from ...domain.user_repository import UserRepository
from ...domain.transfer_objects import CreateActivityTransferObject
from ...domain.entities.activity import Activity
from ...domain.entities.user import User


class ActivityNotExist(Exception):
    pass

class UserNotExist(Exception):
    pass


class CreatingActivityApplicationService:
    """
    Primary port (use case) defining how incoming requests can create the activity
    providing `activity_to`
    """

    def __init__(
        self,
        activity_repository: ActivityRepository,
        user_repository: UserRepository,
        unit_of_work: UnitOfWork,
    ):
        self._activity_repository = activity_repository
        self._user_repository = user_repository
        self._uow = unit_of_work

    def create_activity(self, activity_to: CreateActivityTransferObject) -> None:
        user = self._user_repository.get(activity_to.user_id)
        if not user:
            raise UserNotExist
        with self._uow:
            new_activity = Activity(
                name=activity_to.name, 
                hour=activity_to.hour, 
                date=activity_to.date,
                user=User(id=activity_to.user_id)
                )
            self._activity_repository.add(new_activity)
