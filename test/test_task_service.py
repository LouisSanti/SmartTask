import unittest
from services.task_service import TaskService
from storage.memory_storage import MemoryStorage

class TestTaskService(unittest.TestCase):

    def setUp(self):
        self.storage = MemoryStorage()
        self.service = TaskService(self.storage)

    def test_add_task(self):
        self.service.add_task("Test", "School")
        self.assertEqual(len(self.service.tasks), 1)

    def test_complete_task(self):
        self.service.add_task("Task", "Work")
        self.service.mark_completed(0)
        self.assertTrue(self.service.tasks[0].completed)

    def test_delete_task(self):
        self.service.add_task("Task", "Work")
        self.service.delete_task(0)
        self.assertEqual(len(self.service.tasks), 0)

if __name__ == "__main__":
    unittest.main()
