from typing import List, Optional

from sqlalchemy.orm import Query, Session

from ....domain.entities.categoria import Categoria
from ....domain.categoria_repository import CategoriaRepository


class SQLAlchemyCategoriaRepository(CategoriaRepository):
    """
    Secondary adapter providing ORM SQLAlchemy implementation for :class:`Activity`
    instances storage
    """

    def __init__(self, session: Session):
        self.session = session

    @property
    def queryset(self) -> Query:
        return self.session.query(Categoria)

    def get(self, acti_id: int) -> Optional[Categoria]:
        return self.queryset.get(acti_id)

    def all(self) -> List[Categoria]:
        return self.queryset.all()

    def add(self, categoria: Categoria) -> None:
        self.session.add(categoria)
        self.session.flush()
