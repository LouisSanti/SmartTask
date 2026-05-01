class Task:
    def __init__(self, title, category, completed=False):
        self.title = title
        self.category = category
        self.completed = completed

    def mark_completed(self):
        self.completed = True

    def to_dict(self):
        return {
            "title": self.title,
            "category": self.category,
            "completed": self.completed
        }

    @staticmethod
    def from_dict(data):
        return Task(
            data["title"],
            data["category"],
            data["completed"]
        )

    def __str__(self):
        status = "✔" if self.completed else "✘"
        return f"[{status}] {self.title} ({self.category})"
