from ..uow import UnitOfWork
from ...domain.categoria_repository import CategoriaRepository
from ...domain.transfer_objects import CreateCategoriaTransferObject
from ...domain.entities.categoria import Categoria


class ActivityNotExist(Exception):
    pass

class UserNotExist(Exception):
    pass


class CreatingCategoriaApplicationService:
    """
    Primary port (use case) defining how incoming requests can create the activity
    providing `activity_to`
    """

    def __init__(
        self,
        categoria_repository: CategoriaRepository,
        unit_of_work: UnitOfWork,
    ):
        self._categoria_repository = categoria_repository
        self._uow = unit_of_work

    def create_activity(self, categoria_to: CreateCategoriaTransferObject) -> None:
        with self._uow:
            new_activity = Categoria(
                name=categoria_to.name 
                )
            self._categoria_repository.add(new_activity)
