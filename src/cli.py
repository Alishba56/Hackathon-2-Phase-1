"""
Todo Application - Command Line Interface

This module provides the CLI interface for user interaction:
- TodoCLI: Main CLI class that handles user input and output
"""

from services import TaskService


class TodoCLI:
    """Main CLI interface for the todo application"""

    def __init__(self):
        """Initialize the CLI with a task service"""
        self.task_service = TaskService()

    def display_menu(self):
        """Display the main menu options to the user"""
        print("\n" + "="*40)
        print("TODO APPLICATION")
        print("="*40)
        print("1. Add a new task")
        print("2. View all tasks")
        print("3. Update an existing task")
        print("4. Delete a task")
        print("5. Mark task as complete or incomplete")
        print("6. Exit application")
        print("="*40)

    def get_user_choice(self) -> int:
        """
        Get the user's menu selection

        Returns:
            int: The selected menu option
        """
        while True:
            try:
                choice = int(input("Choose an option (1-6): "))
                if 1 <= choice <= 6:
                    return choice
                else:
                    print("Please enter a number between 1 and 6.")
            except ValueError:
                print("Please enter a valid number.")

    def add_task(self):
        """Add a new task through CLI"""
        try:
            title = input("Enter task title: ").strip()
            if not title:
                print("Task title cannot be empty.")
                return

            description = input("Enter task description (optional): ").strip()

            task = self.task_service.create_task(title, description)
            print(f"Task added successfully with ID: {task['id']}")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An error occurred while adding the task: {e}")

    def display_all_tasks(self):
        """Display all tasks through CLI"""
        tasks = self.task_service.get_all_tasks()

        if not tasks:
            print("\nNo tasks found.")
            return

        print(f"\nTotal tasks: {len(tasks)}")
        for task in tasks:
            status = "Complete" if task['completed'] else "Incomplete"
            print(f"ID: {task['id']} | Title: {task['title']} | Status: {status}")
            if task['description']:
                print(f"     Description: {task['description']}")
        print()

    def update_task(self):
        """Update an existing task through CLI"""
        try:
            task_id = int(input("Enter task ID to update: "))

            if not self.task_service.validate_task_exists(task_id):
                print(f"Task with ID {task_id} does not exist.")
                return

            current_task = self.task_service.get_all_tasks()
            current_task = next((t for t in current_task if t['id'] == task_id), None)
            if not current_task:
                print(f"Task with ID {task_id} does not exist.")
                return

            print(f"Current task: {current_task['title']}")
            new_title = input(f"Enter new title (current: '{current_task['title']}') or press Enter to keep: ").strip()

            print(f"Current description: {current_task['description'] or 'None'}")
            new_description = input("Enter new description or press Enter to keep: ").strip()

            # Use current values if user pressed Enter (empty input)
            title = new_title if new_title else None
            description = new_description if new_description else None

            if self.task_service.update_task(task_id, title, description):
                print("Task updated successfully.")
            else:
                print("Failed to update task.")
        except ValueError:
            print("Please enter a valid task ID.")
        except Exception as e:
            print(f"An error occurred while updating the task: {e}")

    def delete_task(self):
        """Delete a task through CLI"""
        try:
            task_id = int(input("Enter task ID to delete: "))

            if self.task_service.delete_task(task_id):
                print(f"Task {task_id} deleted successfully.")
            else:
                print(f"Task with ID {task_id} does not exist.")
        except ValueError:
            print("Please enter a valid task ID.")
        except Exception as e:
            print(f"An error occurred while deleting the task: {e}")

    def toggle_task_completion(self):
        """Toggle task completion status through CLI"""
        try:
            task_id = int(input("Enter task ID to toggle: "))

            if not self.task_service.validate_task_exists(task_id):
                print(f"Task with ID {task_id} does not exist.")
                return

            if self.task_service.toggle_task_completion(task_id):
                # Get the updated task to show the new status
                updated_task = self.task_service.get_all_tasks()
                task = next((t for t in updated_task if t['id'] == task_id), None)
                if task:
                    status = "Complete" if task['completed'] else "Incomplete"
                    print(f"Task {task_id} status updated to: {status}")
            else:
                print("Failed to toggle task status.")
        except ValueError:
            print("Please enter a valid task ID.")
        except Exception as e:
            print(f"An error occurred while toggling the task: {e}")

    def run(self):
        """Main application loop"""
        print("Welcome to the Todo Application!")

        while True:
            self.display_menu()
            choice = self.get_user_choice()

            if choice == 1:
                self.add_task()
            elif choice == 2:
                self.display_all_tasks()
            elif choice == 3:
                self.update_task()
            elif choice == 4:
                self.delete_task()
            elif choice == 5:
                self.toggle_task_completion()
            elif choice == 6:
                print("Goodbye!")
                break