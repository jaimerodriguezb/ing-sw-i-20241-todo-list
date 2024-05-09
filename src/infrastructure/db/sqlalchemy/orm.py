from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy import Table
from sqlalchemy.orm import mapper, relationship

from ....domain.entities.activity import Activity
from ....domain.entities.user import User

from ....infrastructure.db.sqlalchemy.setup import metadata

activity = Table(
    "activity",
    metadata,
    Column("acti_id", Integer, primary_key=True, autoincrement=True),
    Column("acti_name", String),
    Column("user_id", Integer, ForeignKey("user.user_id")),
)

user = Table(
    "user",
    metadata,
    Column("user_id", Integer, primary_key=True, autoincrement=True),
    Column("user_name", String),
    Column("user_last_name", String),
    Column("user_email", String),
)


def run_mappers():
    """
    Provides mapping between db tables and domain models.
    """
    mapper(
        Activity,
        activity
    )
    mapper(
        User, 
        user,
        properties={"activities": relationship(Activity, backref="user")},
    )