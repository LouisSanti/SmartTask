import json
from models.task import Task
from storage.storage_interface import StorageInterface

class JSONStorage(StorageInterface):

    def __init__(self, filename="tasks.json"):
        self.filename = filename

    def save(self, tasks):
        with open(self.filename, "w") as f:
            json.dump([task.to_dict() for task in tasks], f, indent=4)

    def load(self):
        try:
            with open(self.filename, "r") as f:
                data = json.load(f)
                return [Task.from_dict(item) for item in data]
        except FileNotFoundError:
            return []
