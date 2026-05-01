from storage.json_storage import JSONStorage
from storage.memory_storage import MemoryStorage

class StorageFactory:

    @staticmethod
    def create_storage(storage_type):
        if storage_type == "json":
            return JSONStorage()
        elif storage_type == "memory":
            return MemoryStorage()
        else:
            raise ValueError("Invalid storage type")
