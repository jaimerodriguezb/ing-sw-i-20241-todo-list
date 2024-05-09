from abc import ABC, abstractmethod


class UserRepository(ABC):
    """
    Secondary port defining :class:`User` storage interface
    """

    @abstractmethod
    def get(self, acti_id):
        pass

    @abstractmethod
    def all(self):
        pass

    @abstractmethod
    def add(self, activity):
        pass
