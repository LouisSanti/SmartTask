from models.task import Task

class TaskService:

    def __init__(self, storage):
        self.storage = storage
        self.tasks = self.storage.load()

    def add_task(self, title, category):
        task = Task(title, category)
        self.tasks.append(task)

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)

    def mark_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_completed()

    def filter_by_category(self, category):
        return [t for t in self.tasks if t.category == category]

    def filter_by_status(self, completed=True):
        return [t for t in self.tasks if t.completed == completed]

    def save(self):
        self.storage.save(self.tasks)
