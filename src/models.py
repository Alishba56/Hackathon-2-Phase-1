"""
Todo Application - Data Models

This module defines the data models for the todo application:
- Task: Represents a single todo item
- TodoList: Manages a collection of tasks
"""

from typing import List, Optional


class Task:
    """Represents a single todo item"""

    def __init__(self, task_id: int, title: str, description: str = "", completed: bool = False):
        """
        Initialize a Task instance

        Args:
            task_id (int): Unique identifier for the task
            title (str): Required title of the task
            description (str): Optional description of the task
            completed (bool): Completion status, defaults to False
        """
        if not title or not title.strip():
            raise ValueError("Task title cannot be empty")

        if not isinstance(task_id, int) or task_id <= 0:
            raise ValueError("Task ID must be a positive integer")

        self.id = task_id
        self.title = title.strip()
        self.description = description.strip() if description else ""
        self.completed = completed

    def __str__(self):
        """String representation of the task"""
        status = "Complete" if self.completed else "Incomplete"
        return f"ID: {self.id} | Title: {self.title} | Status: {status}"

    def to_dict(self):
        """Convert task to dictionary representation"""
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "completed": self.completed
        }


class TodoList:
    """Manages a collection of tasks in memory"""

    def __init__(self):
        """Initialize an empty todo list"""
        self.tasks: List[Task] = []
        self._next_id = 1

    def add_task(self, title: str, description: str = "") -> Task:
        """
        Add a new task to the list

        Args:
            title (str): Required title of the task
            description (str): Optional description of the task

        Returns:
            Task: The newly created task
        """
        if not title or not title.strip():
            raise ValueError("Task title cannot be empty")

        task = Task(self._next_id, title, description, False)
        self.tasks.append(task)
        self._next_id += 1
        return task

    def get_all_tasks(self) -> List[Task]:
        """
        Get all tasks in the list

        Returns:
            List[Task]: List of all tasks
        """
        return self.tasks.copy()

    def get_task_by_id(self, task_id: int) -> Optional[Task]:
        """
        Get a task by its ID

        Args:
            task_id (int): The ID of the task to retrieve

        Returns:
            Task or None: The task if found, None otherwise
        """
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

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
        task = self.get_task_by_id(task_id)
        if not task:
            return False

        if title is not None:
            if not title.strip():
                raise ValueError("Task title cannot be empty")
            task.title = title.strip()

        if description is not None:
            task.description = description.strip() if description else ""

        return True

    def delete_task(self, task_id: int) -> bool:
        """
        Delete a task by its ID

        Args:
            task_id (int): The ID of the task to delete

        Returns:
            bool: True if task was deleted, False if task not found
        """
        task = self.get_task_by_id(task_id)
        if not task:
            return False

        self.tasks.remove(task)
        return True

    def toggle_task_completion(self, task_id: int) -> bool:
        """
        Toggle the completion status of a task

        Args:
            task_id (int): The ID of the task to toggle

        Returns:
            bool: True if task status was toggled, False if task not found
        """
        task = self.get_task_by_id(task_id)
        if not task:
            return False

        task.completed = not task.completed
        return True