# Quickstart Guide: In-Memory Todo Python Console Application

**Feature**: 001-todo-app
**Date**: 2026-01-01

## Overview
This guide provides instructions for running and using the in-memory todo console application. The application runs entirely in memory with no persistence, and provides a menu-driven interface for managing tasks.

## Prerequisites
- Python 3.13 or higher
- No external dependencies required (uses only Python standard library)

## Setup
1. Ensure Python 3.13+ is installed on your system
2. Navigate to the project root directory
3. Run the application with: `python src/main.py`

## Usage
The application provides a menu-driven interface with the following options:

### Main Menu Options
1. **Add a new task**
   - Enter a required title for the task
   - Optionally enter a description
   - The system will assign a unique ID automatically

2. **View all tasks**
   - Displays all tasks with their ID, title, and completion status
   - Shows "Complete" or "Incomplete" for each task

3. **Update an existing task**
   - Enter the task ID to identify the task
   - Optionally update the title and/or description
   - Task ID and completion status remain unchanged

4. **Delete a task**
   - Enter the task ID to identify the task to delete
   - Confirms deletion before removing the task

5. **Mark task as complete or incomplete**
   - Enter the task ID to identify the task
   - Toggles the completion status of the task

6. **Exit application**
   - Safely exits the application
   - All data will be lost (in-memory only)

## Example Workflow
```
Welcome to the Todo Application!
1. Add a new task
2. View all tasks
3. Update an existing task
4. Delete a task
5. Mark task as complete or incomplete
6. Exit application

Choose an option: 1
Enter task title: Buy groceries
Enter task description (optional): Need to buy milk and bread
Task added successfully with ID: 1

Choose an option: 2
ID: 1 | Title: Buy groceries | Status: Incomplete
Description: Need to buy milk and bread

Choose an option: 5
Enter task ID to toggle: 1
Task 1 status updated to: Complete

Choose an option: 2
ID: 1 | Title: Buy groceries | Status: Complete
Description: Need to buy milk and bread

Choose an option: 6
Goodbye!
```

## Error Handling
- Invalid task IDs will show appropriate error messages
- Empty titles will be rejected when creating tasks
- Non-existent tasks will show error messages when operations are attempted

## Notes
- All data is stored in memory only and will be lost when the application exits
- Task IDs are auto-generated and unique for the session
- The application is designed for single-user operation