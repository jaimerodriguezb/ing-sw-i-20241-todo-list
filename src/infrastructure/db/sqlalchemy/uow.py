from ....application.uow import UnitOfWork


class SQLAlchemyUnitOfWork(UnitOfWork):
    """
    Secondary adapter providing implementation of transaction management for
    ORM SQLAlchemy
    """

    def __init__(self, session):
        self.session = session

    def __enter__(self):
        return self

    def __exit__(self, *args):
        try:
            self.commit()
        except Exception:
            self.rollback()

    def commit(self):
        self.session.commit()

    def rollback(self):
        self.session.rollback()
