from sqlalchemy.orm import sessionmaker
from ..infrastructure.db.sqlalchemy.setup import engine
from ..infrastructure.db.sqlalchemy.uow import SQLAlchemyUnitOfWork
from ..infrastructure.db.sqlalchemy.activity_repository import SQLAlchemyActivityRepository
from ..infrastructure.db.sqlalchemy.categoria_repository import SQLAlchemyCategoriaRepository
from ..infrastructure.db.sqlalchemy.user_repository import SQLAlchemyUserRepository

Session = sessionmaker(bind=engine)
session = Session()
uow = SQLAlchemyUnitOfWork(session)
activity_repo = SQLAlchemyActivityRepository(session)
categoria_repo = SQLAlchemyCategoriaRepository(session)
user_repo = SQLAlchemyUserRepository(session)