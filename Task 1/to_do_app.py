# File to store tasks
TASKS_FILE = 'tasks.txt'

class Task:
    def __init__(self, task_id, title, description, completed=False):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.completed = completed

    def to_string(self):
        return f"{self.task_id},{self.title},{self.description},{self.completed}\n"

class TodoList:
    def __init__(self):
        self.tasks = self.load_tasks()

    def load_tasks(self):
        tasks = []
        try:
            with open(TASKS_FILE, 'r') as file:
                for line in file:
                    task_data = line.strip().split(',')
                    task = Task(int(task_data[0]), task_data[1], task_data[2], task_data[3] == 'True')
                    tasks.append(task)
        except FileNotFoundError:
            pass  # If the file doesn't exist, return an empty list
        return tasks

    def save_tasks(self):
        with open(TASKS_FILE, 'w') as file:
            for task in self.tasks:
                file.write(task.to_string())

    def display_tasks(self):
        if not self.tasks:
            print("No tasks found.")
        else:
            for task in self.tasks:
                print(f"ID: {task.task_id}, Title: {task.title}, Description: {task.description}, Completed: {task.completed}")

    def add_task(self, title, description):
        task_id = len(self.tasks) + 1
        new_task = Task(task_id, title, description)
        self.tasks.append(new_task)
        self.save_tasks()
        print(f"Task '{title}' added successfully!")

    def mark_task_complete(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                task.completed = True
                self.save_tasks()
                print(f"Task '{task.title}' marked as complete!")
                return
        print(f"Task with ID {task_id} not found.")

    def delete_task(self, task_id):
        self.tasks = [task for task in self.tasks if task.task_id != task_id]
        self.update_task_ids()
        self.save_tasks()
        print(f"Task with ID {task_id} deleted successfully!")

    def update_task_ids(self):
        for index, task in enumerate(self.tasks, start=1):
            task.task_id = index

def main():
    todo_list = TodoList()

    while True:
        print("\n===== To-Do List Menu =====")
        print("1. List Tasks")
        print("2. Add Task")
        print("3. Mark Task as Complete")
        print("4. Delete Task")
        print("5. Quit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            todo_list.display_tasks()
        elif choice == '2':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            todo_list.add_task(title, description)
        elif choice == '3':
            task_id = int(input("Enter task ID to mark as complete: "))
            todo_list.mark_task_complete(task_id)
        elif choice == '4':
            task_id = int(input("Enter task ID to delete: "))
            todo_list.delete_task(task_id)
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
