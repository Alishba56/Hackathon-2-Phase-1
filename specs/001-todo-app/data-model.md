# Data Model: In-Memory Todo Python Console Application

**Feature**: 001-todo-app
**Date**: 2026-01-01
**Status**: Complete

## Entity: Task

### Fields
- **id**: Integer (required, unique, auto-incremented)
  - Purpose: Unique identifier for the task
  - Constraints: Positive integer, unique within the application session
  - Validation: Must be a positive integer

- **title**: String (required)
  - Purpose: Descriptive name of the task
  - Constraints: Non-empty string
  - Validation: Must not be empty or only whitespace

- **description**: String (optional)
  - Purpose: Additional details about the task
  - Constraints: Optional field, can be empty
  - Validation: Can be empty or contain any text

- **completed**: Boolean (required, default: False)
  - Purpose: Status indicator for task completion
  - Constraints: Boolean value (True/False)
  - Validation: Must be a boolean value, defaults to False when created

### Relationships
- The Task entity exists independently within the application
- Tasks are managed as a collection in the TodoList

## Entity: TodoList (Collection)

### Fields
- **tasks**: List of Task objects
  - Purpose: In-memory storage of all tasks
  - Constraints: Contains only Task objects
  - Validation: Maintains uniqueness of task IDs

### State Transitions
- **Task Creation**: New Task object is added to the tasks list with:
  - Auto-generated unique ID
  - Provided title
  - Provided description (or empty string)
  - completed status set to False

- **Task Completion Toggle**:
  - From incomplete (False) to complete (True)
  - From complete (True) to incomplete (False)

### Validation Rules
- Task title must not be empty or only whitespace
- Task ID must be unique within the TodoList
- Task must exist before update/delete operations
- Task ID must be a valid integer when referenced

### Business Rules
- New tasks are created with completed=False by default
- Task IDs are auto-incremented based on the current highest ID
- Tasks can be updated with new title/description while preserving ID
- Tasks can be deleted by referencing their ID
- Task completion status can be toggled by referencing their ID