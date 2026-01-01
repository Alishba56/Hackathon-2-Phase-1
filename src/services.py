"""
Todo Application - Business Services

This module contains the business logic for managing tasks:
- TaskService: Handles all task-related operations
"""

from typing import List, Dict, Any, Optional
from models import TodoList, Task


class TaskService:
    """Handles all task-related business operations"""

    def __init__(self):
        """Initialize the task service with a todo list"""
        self.todo_list = TodoList()

    def create_task(self, title: str, description: str = "") -> Dict[str, Any]:
        """
        Create a new task

        Args:
            title (str): Required title of the task
            description (str): Optional description of the task

        Returns:
            dict: Dictionary containing the created task data
        """
        task = self.todo_list.add_task(title, description)
        return task.to_dict()

    def get_all_tasks(self) -> List[Dict[str, Any]]:
        """
        Get all tasks

        Returns:
            List[dict]: List of all tasks as dictionaries
        """
        tasks = self.todo_list.get_all_tasks()
        return [task.to_dict() for task in tasks]

    def update_task(self, task_id: int, title: Optional[str] = None, description: Optional[str] = None) -> bool:
        """
        Update an existing task

        Args:
            task_id (int): The ID of the task to update
            title (str, optional): New title if provided
            description (str, optional): New description if provided

        Returns:
            bool: True if task was updated, False if task not found
        """
        return self.todo_list.update_task(task_id, title, description)

    def delete_task(self, task_id: int) -> bool:
        """
        Delete a task by its ID

        Args:
            task_id (int): The ID of the task to delete

        Returns:
            bool: True if task was deleted, False if task not found
        """
        return self.todo_list.delete_task(task_id)

    def toggle_task_completion(self, task_id: int) -> bool:
        """
        Toggle the completion status of a task

        Args:
            task_id (int): The ID of the task to toggle

        Returns:
            bool: True if task status was toggled, False if task not found
        """
        return self.todo_list.toggle_task_completion(task_id)

    def validate_task_exists(self, task_id: int) -> bool:
        """
        Check if a task exists

        Args:
            task_id (int): The ID of the task to check

        Returns:
            bool: True if task exists, False otherwise
        """
        return self.todo_list.get_task_by_id(task_id) is not None