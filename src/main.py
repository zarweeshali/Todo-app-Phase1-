"""
Main CLI interface for the Todo application.
"""

import sys
from src.services.task_service import TaskService


def main():
    """
    Main entry point for the Todo CLI application.
    """
    print("Welcome to the Todo CLI App!")
    print("Type 'help' for available commands or 'exit' to quit.")
    
    task_service = TaskService()
    
    while True:
        try:
            # Display prompt and read user input
            user_input = input("todo> ").strip()
            
            if not user_input:
                continue
            
            # Parse the command
            parts = user_input.split(maxsplit=1)
            command = parts[0].lower()
            
            # Handle the command
            if command == "exit":
                print("Goodbye!")
                break
            elif command == "help":
                show_help()
            elif command == "add":
                handle_add(task_service, parts[1] if len(parts) > 1 else "")
            elif command == "list":
                handle_list(task_service)
            elif command == "update":
                handle_update(task_service, parts[1] if len(parts) > 1 else "")
            elif command == "delete":
                handle_delete(task_service, parts[1] if len(parts) > 1 else "")
            elif command == "complete":
                handle_complete(task_service, parts[1] if len(parts) > 1 else "")
            elif command == "incomplete":
                handle_incomplete(task_service, parts[1] if len(parts) > 1 else "")
            else:
                print("Error: Invalid command")
                
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except EOFError:
            print("\nGoodbye!")
            break


def show_help():
    """
    Display help information for available commands.
    """
    help_text = """
Available commands:
  add "title" "optional description" - Add a new task
  list - Show all tasks
  update id "new title" "new description" - Update a task
  delete id - Delete a task
  complete id - Mark task as complete
  incomplete id - Mark task as incomplete
  help - Show this help message
  exit - Quit the application
"""
    print(help_text.strip())


def handle_add(task_service, args_str):
    """
    Handle the 'add' command.
    
    Args:
        task_service (TaskService): The task service instance
        args_str (str): Arguments string containing title and description
    """
    try:
        # Parse title and description from the arguments
        args = parse_args(args_str, expected_count=2)
        if not args or not args[0]:
            print("Error: Title is required")
            return
        
        title = args[0]
        description = args[1] if len(args) > 1 else ""
        
        task = task_service.add_task(title, description)
        print(f"Task {task.id} created: {task.title}")
    except Exception as e:
        print(f"Error: {str(e)}")


def handle_list(task_service):
    """
    Handle the 'list' command.
    
    Args:
        task_service (TaskService): The task service instance
    """
    try:
        tasks = task_service.get_all_tasks()
        if not tasks:
            print("(No tasks)")
        else:
            for task in tasks:
                print(task)
    except Exception as e:
        print(f"Error: {str(e)}")


def handle_update(task_service, args_str):
    """
    Handle the 'update' command.
    
    Args:
        task_service (TaskService): The task service instance
        args_str (str): Arguments string containing task ID, new title, and new description
    """
    try:
        args = parse_args(args_str, expected_count=3)
        if len(args) < 2:
            print("Error: Task ID and at least one field to update are required")
            return
        
        task_id = int(args[0])
        new_title = args[1] if len(args) > 1 and args[1] else None
        new_description = args[2] if len(args) > 2 and args[2] else None
        
        task_service.update_task(task_id, new_title, new_description)
        print(f"Task {task_id} updated")
    except ValueError:
        print("Error: Task ID must be a number")
    except Exception as e:
        print(f"Error: {str(e)}")


def handle_delete(task_service, args_str):
    """
    Handle the 'delete' command.
    
    Args:
        task_service (TaskService): The task service instance
        args_str (str): Arguments string containing task ID
    """
    try:
        args = parse_args(args_str, expected_count=1)
        if not args or not args[0]:
            print("Error: Task ID is required")
            return
        
        task_id = int(args[0])
        task_service.delete_task(task_id)
        print(f"Task {task_id} deleted")
    except ValueError:
        print("Error: Task ID must be a number")
    except Exception as e:
        print(f"Error: {str(e)}")


def handle_complete(task_service, args_str):
    """
    Handle the 'complete' command.
    
    Args:
        task_service (TaskService): The task service instance
        args_str (str): Arguments string containing task ID
    """
    try:
        args = parse_args(args_str, expected_count=1)
        if not args or not args[0]:
            print("Error: Task ID is required")
            return
        
        task_id = int(args[0])
        task_service.complete_task(task_id)
        print(f"Task {task_id} marked complete")
    except ValueError:
        print("Error: Task ID must be a number")
    except Exception as e:
        print(f"Error: {str(e)}")


def handle_incomplete(task_service, args_str):
    """
    Handle the 'incomplete' command.
    
    Args:
        task_service (TaskService): The task service instance
        args_str (str): Arguments string containing task ID
    """
    try:
        args = parse_args(args_str, expected_count=1)
        if not args or not args[0]:
            print("Error: Task ID is required")
            return
        
        task_id = int(args[0])
        task_service.incomplete_task(task_id)
        print(f"Task {task_id} marked incomplete")
    except ValueError:
        print("Error: Task ID must be a number")
    except Exception as e:
        print(f"Error: {str(e)}")


def parse_args(args_str, expected_count=None):
    """
    Parse quoted arguments from a string.
    
    Args:
        args_str (str): The string containing quoted arguments
        expected_count (int, optional): Expected number of arguments
    
    Returns:
        list: List of parsed arguments
    """
    args = []
    current_arg = ""
    in_quotes = False
    i = 0
    
    while i < len(args_str):
        char = args_str[i]
        
        if char == '"':
            in_quotes = not in_quotes
        elif char == ' ' and not in_quotes:
            if current_arg or len(args) > 0:  # Don't add empty args unless it's the first one
                args.append(current_arg)
                current_arg = ""
        else:
            current_arg += char
        
        i += 1
    
    # Add the last argument if it exists
    if current_arg or in_quotes:
        args.append(current_arg)
    
    # If expected_count is provided, pad with empty strings if needed
    if expected_count and len(args) < expected_count:
        args.extend([""] * (expected_count - len(args)))
    
    return args


if __name__ == "__main__":
    main()