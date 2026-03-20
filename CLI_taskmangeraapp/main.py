from app.task_manager import TaskManager
from app.storage import save_tasks, load_tasks


def display_menu():
    print("\n=== TASK MANAGER ===")
    print("1. View tasks")
    print("2. Add task")
    print("3. Complete task")
    print("4. Delete task")
    print("5. Exit")

# Helper functions 
def get_valid_task_id(prompt):
    while True:
        user_input = input(prompt)

        if user_input.isdigit():
            return int(user_input)
        print("Please enter a valud numeric task ID")

def get_non_empty_title(prompt):
    while True:
        title = input(prompt).strip()

        if title:
            return title

        print("Task title cannot be empty.")


def main():
    manager = TaskManager()
    manager.tasks = load_tasks()

    while True:
        display_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            tasks = manager.show_tasks()
            if not tasks:
                print("No tasks found.")
            else:
                print("\nCurrent tasks:")
                for task in tasks:
                    print(task)

        elif choice == "2":
            title = get_non_empty_title("Enter task title: ")
            new_task = manager.add_task(title)
            save_tasks(manager.tasks)
            print(f'Task added: {new_task}')

        elif choice == "3":
            task_id = get_valid_task_id("Enter task ID to complete: ")
            message = manager.complete_tasks(task_id)
            save_tasks(manager.tasks)
            print(message)

        elif choice == "4":
            task_id = get_valid_task_id("Enter task ID to delete: ")
            deleted = manager.delete_task(task_id)

            if deleted:
                save_tasks(manager.tasks)
                print(f"Task {task_id} deleted.")
            else:
                print(f"Task {task_id} not found.")

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please choose 1 to 5.")


if __name__ == "__main__":
    main()