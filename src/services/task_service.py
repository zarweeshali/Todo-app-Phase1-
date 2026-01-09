"""
TaskService implementing business logic for task management.
"""

from src.models.task import Task


class TaskService:
    """
    Service layer for managing tasks with business logic.
    """
    
    def __init__(self):
        """
        Initialize the TaskService with an empty in-memory collection.
        """
        self.tasks = {}
        self.next_id = 1
    
    def add_task(self, title, description=""):
        """
        Add a new task to the collection.
        
        Args:
            title (str): Required task name
            description (str, optional): Additional details about the task. Defaults to "".
        
        Returns:
            Task: The newly created task with assigned ID
        
        Raises:
            ValueError: If title is empty
        """
        if not title or not title.strip():
            raise ValueError("Title is required")
        
        task = Task(self.next_id, title.strip(), description)
        self.tasks[self.next_id] = task
        self.next_id += 1
        return task
    
    def get_task(self, task_id):
        """
        Retrieve a task by its ID.
        
        Args:
            task_id (int): The ID of the task to retrieve
        
        Returns:
            Task: The task with the specified ID
        
        Raises:
            KeyError: If no task exists with the specified ID
        """
        if task_id not in self.tasks:
            raise KeyError(f"Task with ID {task_id} not found")
        return self.tasks[task_id]
    
    def get_all_tasks(self):
        """
        Retrieve all tasks in the collection.
        
        Returns:
            list: List of all Task objects sorted by ID
        """
        return sorted(self.tasks.values(), key=lambda task: task.id)
    
    def update_task(self, task_id, title=None, description=None):
        """
        Update an existing task's title and/or description.
        
        Args:
            task_id (int): The ID of the task to update
            title (str, optional): New title for the task
            description (str, optional): New description for the task
        
        Returns:
            Task: The updated task
        
        Raises:
            KeyError: If no task exists with the specified ID
        """
        if task_id not in self.tasks:
            raise KeyError(f"Task with ID {task_id} not found")
        
        task = self.tasks[task_id]
        
        if title is not None:
            task.title = title.strip() if title.strip() else task.title
        
        if description is not None:
            task.description = description
        
        return task
    
    def delete_task(self, task_id):
        """
        Remove a task from the collection.
        
        Args:
            task_id (int): The ID of the task to delete
        
        Returns:
            Task: The deleted task
        
        Raises:
            KeyError: If no task exists with the specified ID
        """
        if task_id not in self.tasks:
            raise KeyError(f"Task with ID {task_id} not found")
        
        deleted_task = self.tasks.pop(task_id)
        return deleted_task
    
    def complete_task(self, task_id):
        """
        Mark a task as complete.
        
        Args:
            task_id (int): The ID of the task to mark complete
        
        Returns:
            Task: The updated task marked as complete
        
        Raises:
            KeyError: If no task exists with the specified ID
        """
        if task_id not in self.tasks:
            raise KeyError(f"Task with ID {task_id} not found")
        
        task = self.tasks[task_id]
        task.completed = True
        return task
    
    def incomplete_task(self, task_id):
        """
        Mark a task as incomplete.
        
        Args:
            task_id (int): The ID of the task to mark incomplete
        
        Returns:
            Task: The updated task marked as incomplete
        
        Raises:
            KeyError: If no task exists with the specified ID
        """
        if task_id not in self.tasks:
            raise KeyError(f"Task with ID {task_id} not found")
        
        task = self.tasks[task_id]
        task.completed = False
        return task