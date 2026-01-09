# CLI Command Contracts: Todo CLI App

**Feature**: Todo CLI App
**Date**: 2026-01-09
**Version**: 1.0

## Overview

This document defines the command-line interface contracts for the Todo CLI application. These contracts specify the expected input format, output format, and behavior for each command.

## Command Definitions

### ADD Command
**Syntax**: `add "title" "optional description"`

**Input**:
- Positional argument 1: title (string, required)
- Positional argument 2: description (string, optional)

**Output**:
- Success: `Task {id} created: {title}`
- Error: `Error: Title is required` (if title is missing)

**Behavior**:
- Creates a new task with the provided title and description
- Assigns the next available ID
- Sets completion status to false by default
- Adds task to in-memory collection

### LIST Command
**Syntax**: `list`

**Input**: None

**Output**:
- Success: Formatted list of all tasks in the format `[ ] {id}: {title} — {description}` or `[x] {id}: {title} — {description}` for completed tasks
- Error: None

**Behavior**:
- Retrieves all tasks from in-memory collection
- Formats and displays each task with its ID, completion status, title, and description
- Uses `[ ]` for incomplete tasks and `[x]` for completed tasks

### UPDATE Command
**Syntax**: `update {id} "new title" "new description"`

**Input**:
- Positional argument 1: task ID (integer, required)
- Positional argument 2: new title (string, optional)
- Positional argument 3: new description (string, optional)

**Output**:
- Success: `Task {id} updated`
- Error: `Error: Task not found` (if task doesn't exist)

**Behavior**:
- Updates only the fields that are provided
- Leaves other fields unchanged
- Validates that the task exists before updating

### DELETE Command
**Syntax**: `delete {id}`

**Input**:
- Positional argument 1: task ID (integer, required)

**Output**:
- Success: `Task {id} deleted`
- Error: `Error: Task not found` (if task doesn't exist)

**Behavior**:
- Removes the specified task from in-memory collection
- Validates that the task exists before deletion

### COMPLETE Command
**Syntax**: `complete {id}`

**Input**:
- Positional argument 1: task ID (integer, required)

**Output**:
- Success: `Task {id} marked complete`
- Error: `Error: Task not found` (if task doesn't exist)

**Behavior**:
- Updates the completion status of the specified task to true
- Validates that the task exists before updating

### INCOMPLETE Command
**Syntax**: `incomplete {id}`

**Input**:
- Positional argument 1: task ID (integer, required)

**Output**:
- Success: `Task {id} marked incomplete`
- Error: `Error: Task not found` (if task doesn't exist)

**Behavior**:
- Updates the completion status of the specified task to false
- Validates that the task exists before updating

### EXIT Command
**Syntax**: `exit`

**Input**: None

**Output**: Exits the application

**Behavior**:
- Terminates the application gracefully
- No data is persisted (as per Phase I constraints)