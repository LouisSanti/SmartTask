from storage.storage_interface import StorageInterface

class MemoryStorage(StorageInterface):

    def __init__(self):
        self.tasks = []

    def save(self, tasks):
        self.tasks = tasks

    def load(self):
        return self.tasks
