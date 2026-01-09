# Quickstart Guide: Todo CLI App

**Feature**: Todo CLI App
**Date**: 2026-01-09

## Getting Started

To run the Todo CLI application:

1. Ensure Python 3.9+ is installed on your system
2. Navigate to the project root directory
3. Run the application:

```bash
python main.py
```

## Available Commands

Once the application is running, you'll see the `todo> ` prompt. Enter one of the following commands:

### Add a Task
```bash
add "Task Title" "Optional Description"
```

Example:
```bash
add "Buy groceries" "Milk and eggs"
```

### List All Tasks
```bash
list
```

This will show all tasks with their ID, completion status, title, and description.

### Update a Task
```bash
update <task_id> "New Title" "New Description"
```

Example:
```bash
update 1 "Updated task title" "Updated description"
```

### Delete a Task
```bash
delete <task_id>
```

Example:
```bash
delete 1
```

### Mark Task as Complete
```bash
complete <task_id>
```

Example:
```bash
complete 1
```

### Mark Task as Incomplete
```bash
incomplete <task_id>
```

Example:
```bash
incomplete 1
```

### Exit the Application
```bash
exit
```

## Example Session

```
todo> add "Buy groceries" "Milk and eggs"
Task 1 created: Buy groceries
todo> add "Call mom"
Task 2 created: Call mom
todo> list
[ ] 1: Buy groceries — Milk and eggs
[ ] 2: Call mom —
todo> complete 1
Task 1 marked complete
todo> list
[x] 1: Buy groceries — Milk and eggs
[ ] 2: Call mom —
todo> exit
```

## Error Messages

The application will display error messages for invalid operations:

- `Error: Task not found` - when referencing a non-existent task ID
- `Error: Invalid command` - when entering an unrecognized command
- `Error: Title is required` - when adding a task without a title