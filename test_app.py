import sys
import os
sys.path.insert(0, os.getcwd())

from src.services.task_service import TaskService

print("Testing TaskService functionality:")

# Create a task service instance
task_service = TaskService()

# Add a task
task = task_service.add_task("Test task", "Test description")
print(f"Added task: {task}")

# Complete the task
task_service.complete_task(task.id)
print(f"After completing: {task}")

# List all tasks
all_tasks = task_service.get_all_tasks()
print(f"All tasks: {len(all_tasks)}")

print("TaskService working correctly!")