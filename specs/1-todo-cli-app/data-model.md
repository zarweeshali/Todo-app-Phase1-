# Data Model: Todo CLI App

**Feature**: Todo CLI App
**Date**: 2026-01-09
**Status**: Final

## Entities

### Task

**Description**: Represents a user's task with ID, title, description, and completion status

**Fields**:
- `id`: Integer, required, auto-incremented unique identifier
- `title`: String, required, task name
- `description`: String, optional, additional details about the task
- `completed`: Boolean, required, completion status (defaults to false)

**Validation Rules**:
- `id` must be a positive integer
- `title` must be a non-empty string (1-255 characters)
- `description` can be empty or a string up to 1000 characters
- `completed` must be a boolean value

**State Transitions**:
- `completed` can transition from `false` to `true` (complete operation)
- `completed` can transition from `true` to `false` (incomplete operation)

**Relationships**:
- None (standalone entity)

## Data Flow

### Creation
1. User provides title and optional description
2. System assigns next available ID
3. System sets completed to false by default
4. Task is stored in in-memory collection

### Reading
1. Tasks retrieved from in-memory collection
2. All fields returned for display

### Updating
1. User specifies task ID and new title/description values
2. System validates existence of task
3. System updates specified fields only
4. Other fields remain unchanged

### Deletion
1. User specifies task ID
2. System validates existence of task
3. System removes task from in-memory collection

### Status Change
1. User specifies task ID and desired completion status
2. System validates existence of task
3. System updates completed field
4. Other fields remain unchanged