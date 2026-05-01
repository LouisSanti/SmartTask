from factory.storage_factory import StorageFactory
from services.task_service import TaskService

def display_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return

    for i, t in enumerate(tasks):
        status = "✔" if t.completed else "✘"
        print(f"{i}. [{status}] {t.title} ({t.category})")

def main():
    storage = StorageFactory.create_storage("json")
    service = TaskService(storage)

    while True:
        print("\n==== SmartTask Menu ====")
        print("1. Add Task")
        print("2. View All Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Filter by Category")
        print("6. Filter by Status")
        print("7. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            title = input("Enter task title: ")
            category = input("Enter category (School/Work/Personal): ")
            service.add_task(title, category)

        elif choice == "2":
            display_tasks(service.tasks)

        elif choice == "3":
            display_tasks(service.tasks)
            index = int(input("Enter task index: "))
            service.mark_completed(index)

        elif choice == "4":
            display_tasks(service.tasks)
            index = int(input("Enter task index: "))
            service.delete_task(index)

        elif choice == "5":
            category = input("Enter category: ")
            tasks = service.filter_by_category(category)
            display_tasks(tasks)

        elif choice == "6":
            status = input("Completed only? (y/n): ").lower() == "y"
            tasks = service.filter_by_status(status)
            display_tasks(tasks)

        elif choice == "7":
            service.save()
            print("Tasks saved. Goodbye!")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()