from dataclasses import dataclass
from datetime import datetime

from .value_objects import ActivityId
from .value_objects import CategoryId

@dataclass(frozen=True)
class TransferObject:
    pass


@dataclass(frozen=True)
class CreateActivityTransferObject(TransferObject):
    name: str
    hour: datetime.time
    date: datetime.date
    user_id: int


@dataclass(frozen=True)
class CreateCategoriaTransferObject(TransferObject):
    name: str
    
