# Todo CLI App

A command-line todo application that operates entirely in memory. The application follows clean architecture with domain, service, and interface layers, allowing users to add, list, update, delete, and mark tasks as complete/incomplete.

## Features

- Add new tasks with titles and optional descriptions
- List all tasks with their completion status
- Update existing tasks
- Delete tasks
- Mark tasks as complete or incomplete
- All data stored in memory (lost when program exits)

## Usage

To run the application:

```bash
python src/cli/main.py
```

Once running, you'll see the `todo> ` prompt. Available commands:

- `add "title" "optional description"` - Add a new task
- `list` - Show all tasks
- `update <id> "new title" "new description"` - Update a task
- `delete <id>` - Delete a task
- `complete <id>` - Mark task as complete
- `incomplete <id>` - Mark task as incomplete
- `exit` - Quit the application

Example session:

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

## Architecture

This application follows clean architecture principles:

- **Domain Layer**: Task entity in `src/models/task.py`
- **Service Layer**: TaskService with business logic in `src/services/task_service.py`
- **Interface Layer**: CLI interface in `src/cli/main.py`

## Development

This project is structured with:

- Source code in the `src/` directory
- Unit tests in `tests/unit/`
- Integration tests in `tests/integration/`