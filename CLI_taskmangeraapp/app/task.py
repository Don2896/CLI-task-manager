import random

class Task:
    def __init__(self, title, task_id=0 ,status="incomplete"):
        self.title = title
        self.task_id = task_id
        self.status = status


    def __str__(self):
        return f'[{self.task_id}] - {self.title} - {self.status}'
    
    def to_dict(self):
        
        return {
            "task_id": self.task_id,
            "title": self.title,
            "status": self.status
            }
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            task_id=data["task_id"],
            title=data["title"],
            status=data["status"]
        )
