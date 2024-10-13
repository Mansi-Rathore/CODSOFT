class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f'Task "{task}" added.')

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the to-do list.")
        else:
            print("To-Do List:")
            for idx, task in enumerate(self.tasks, start=1):
                print(f"{idx}. {task}")

    def update_task(self, index, new_task):
        if 0 <= index < len(self.tasks):
            old_task = self.tasks[index]
            self.tasks[index] = new_task
            print(f'Task "{old_task}" updated to "{new_task}".')
        else:
            print("Invalid task index.")

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            removed_task = self.tasks.pop(index)
            print(f'Task "{removed_task}" removed.')
        else:
            print("Invalid task index.")

def main():
    todo_list = TodoList()
    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == '1':
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == '2':
            todo_list.view_tasks()
        elif choice == '3':
            todo_list.view_tasks()
            index = int(input("Enter the task number to update: ")) - 1
            new_task = input("Enter the new task: ")
            todo_list.update_task(index, new_task)
        elif choice == '4':
            todo_list.view_tasks()
            index = int(input("Enter the task number to delete: ")) - 1
            todo_list.delete_task(index)
        elif choice == '5':
            print("Exiting the To-Do List application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
