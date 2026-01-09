"""
Task entity model representing a user's task with ID, title, description, and completion status.
"""

class Task:
    """
    Represents a user's task with ID, title, description, and completion status.
    """
    
    def __init__(self, task_id, title, description="", completed=False):
        """
        Initialize a Task instance.
        
        Args:
            task_id (int): Unique identifier for the task
            title (str): Required task name
            description (str, optional): Additional details about the task. Defaults to "".
            completed (bool, optional): Completion status. Defaults to False.
        
        Raises:
            ValueError: If title is empty or task_id is not a positive integer
        """
        if not title or not isinstance(title, str):
            raise ValueError("Title must be a non-empty string")
        
        if not isinstance(task_id, int) or task_id <= 0:
            raise ValueError("Task ID must be a positive integer")
        
        self.id = task_id
        self.title = title.strip()
        self.description = description or ""
        self.completed = completed
    
    def __str__(self):
        """
        String representation of the task.
        """
        status = "[x]" if self.completed else "[ ]"
        return f"{status} {self.id}: {self.title} — {self.description}"
    
    def __repr__(self):
        """
        Developer-friendly representation of the task.
        """
        return f"Task(id={self.id}, title='{self.title}', description='{self.description}', completed={self.completed})"
    
    def to_dict(self):
        """
        Convert the task to a dictionary representation.
        
        Returns:
            dict: Dictionary representation of the task
        """
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "completed": self.completed
        }
    
    @classmethod
    def from_dict(cls, data):
        """
        Create a Task instance from a dictionary.
        
        Args:
            data (dict): Dictionary containing task data
        
        Returns:
            Task: Task instance created from the dictionary
        """
        return cls(
            task_id=data["id"],
            title=data["title"],
            description=data.get("description", ""),
            completed=data.get("completed", False)
        )