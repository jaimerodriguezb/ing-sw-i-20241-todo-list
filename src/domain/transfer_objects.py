from dataclasses import dataclass
from datetime import datetime

from .value_objects import ActivityId


@dataclass(frozen=True)
class TransferObject:
    pass


@dataclass(frozen=True)
class CreateActivityTransferObject(TransferObject):
    name: str
    hour: datetime.time
    date: datetime.date
    user_id: int
