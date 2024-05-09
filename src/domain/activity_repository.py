from abc import ABC, abstractmethod


class ActivityRepository(ABC):
    """
    Secondary port defining :class:`Activity` storage interface
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
