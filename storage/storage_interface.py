from abc import ABC, abstractmethod

class StorageInterface(ABC):

    @abstractmethod
    def save(self, tasks):
        pass

    @abstractmethod
    def load(self):
        pass
