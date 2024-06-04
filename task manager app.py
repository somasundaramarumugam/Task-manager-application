class Task:
    id_counter = 1

    def __init__(self, title, description, priority, status):
        self.id = Task.id_counter
        Task.id_counter += 1
        self.title = title
        self.description = description
        self.priority = priority
        self.status = status

    def __str__(self):
        return (f"ID: {self.id}\n"
                f"Title: {self.title}\n"
                f"Description: {self.description}\n"
                f"Priority: {self.priority}\n"
                f"Status: {self.status}\n")


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description, priority, status):
        task = Task(title, description, priority, status)
        self.tasks.append(task)
        print(f"Task '{title}' added successfully.\n")

    def edit_task(self, task_id, title=None, description=None, priority=None, status=None):
        task = self.get_task_by_id(task_id)
        if task:
            if title:
                task.title = title
            if description:
                task.description = description
            if priority:
                task.priority = priority
            if status:
                task.status = status
            print(f"Task ID {task_id} updated successfully.\n")
        else:
            print(f"Task ID {task_id} not found.\n")

    def delete_task(self, task_id):
        task = self.get_task_by_id(task_id)
        if task:
            self.tasks.remove(task)
            print(f"Task ID {task_id} deleted successfully.\n")
        else:
            print(f"Task ID {task_id} not found.\n")

    def get_task_by_id(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def view_all_tasks(self):
        if not self.tasks:
            print("No tasks available.\n")
        else:
            for task in self.tasks:
                print(task)

    def filter_tasks_by_priority(self, priority):
        filtered_tasks = [task for task in self.tasks if task.priority.lower() == priority.lower()]
        if not filtered_tasks:
            print(f"No tasks with priority '{priority}' found.\n")
        else:
            for task in filtered_tasks:
                print(task)


def main():
    task_manager = TaskManager()

    while True:
        print("Task Manager Menu:")
        print("1. Add Task")
        print("2. Edit Task")
        print("3. Delete Task")
        print("4. View All Tasks")
        print("5. Filter Tasks by Priority")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter title: ")
            description = input("Enter description: ")
            priority = input("Enter priority (High/Medium/Low): ")
            status = input("Enter status (Pending/In Progress/Completed): ")
            task_manager.add_task(title, description, priority, status)

        elif choice == '2':
            try:
                task_id = int(input("Enter task ID to edit: "))
                title = input("Enter new title (leave blank to keep unchanged): ")
                description = input("Enter new description (leave blank to keep unchanged): ")
                priority = input("Enter new priority (High/Medium/Low) (leave blank to keep unchanged): ")
                status = input("Enter new status (Pending/In Progress/Completed) (leave blank to keep unchanged): ")
                task_manager.edit_task(task_id, title, description, priority, status)
            except ValueError:
                print("Invalid input. Task ID should be a number.\n")

        elif choice == '3':
            try:
                task_id = int(input("Enter task ID to delete: "))
                task_manager.delete_task(task_id)
            except ValueError:
                print("Invalid input. Task ID should be a number.\n")

        elif choice == '4':
            task_manager.view_all_tasks()

        elif choice == '5':
            priority = input("Enter priority to filter by (High/Medium/Low): ")
            task_manager.filter_tasks_by_priority(priority)

        elif choice == '6':
            print("Exiting Task Manager. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.\n")


if __name__ == "__main__":
    main()
