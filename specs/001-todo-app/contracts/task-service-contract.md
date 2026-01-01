# API Contracts: Todo Application

**Feature**: 001-todo-app
**Date**: 2026-01-01

## Overview
This document defines the functional contracts for the in-memory todo console application. Since this is a CLI application, the "contracts" represent the function signatures and expected behaviors of the core services.

## Service Contracts

### TaskService

#### create_task(title: str, description: str = "") -> dict
**Purpose**: Creates a new task with the provided title and optional description
**Input**:
- title (str): Required task title, must not be empty
- description (str): Optional task description, defaults to empty string
**Output**: Dictionary containing the created task with fields: id, title, description, completed
**Behavior**:
- Assigns a unique auto-incremented ID
- Sets completion status to False by default
- Validates that title is not empty
- Returns the complete task object

#### get_all_tasks() -> list
**Purpose**: Retrieves all tasks in the todo list
**Input**: None
**Output**: List of task dictionaries, each containing id, title, description, completed
**Behavior**:
- Returns all tasks in the current session
- Returns empty list if no tasks exist
- Maintains order of task creation

#### update_task(task_id: int, title: str = None, description: str = None) -> bool
**Purpose**: Updates an existing task's title and/or description
**Input**:
- task_id (int): The ID of the task to update
- title (str, optional): New title if provided
- description (str, optional): New description if provided
**Output**: Boolean indicating success (True) or failure (False)
**Behavior**:
- Updates only the fields that are provided
- Preserves other fields unchanged
- Returns False if task with given ID doesn't exist

#### delete_task(task_id: int) -> bool
**Purpose**: Removes a task from the todo list
**Input**:
- task_id (int): The ID of the task to delete
**Output**: Boolean indicating success (True) or failure (False)
**Behavior**:
- Removes the task from the list
- Returns False if task with given ID doesn't exist

#### toggle_task_completion(task_id: int) -> bool
**Purpose**: Toggles the completion status of a task
**Input**:
- task_id (int): The ID of the task to update
**Output**: Boolean indicating success (True) or failure (False)
**Behavior**:
- Changes completed status from True to False or False to True
- Returns False if task with given ID doesn't exist

## CLI Contracts

### CLI Interface

#### display_menu() -> None
**Purpose**: Shows the main menu options to the user
**Input**: None
**Output**: Displays menu to console
**Behavior**:
- Shows numbered options for all available operations
- Includes option to exit the application

#### get_user_choice() -> int
**Purpose**: Gets the user's menu selection
**Input**: User input from console
**Output**: Integer representing the selected option
**Behavior**:
- Validates that input is a valid menu option
- Prompts again if input is invalid