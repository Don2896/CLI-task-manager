

from app.task import Task
import random

class TaskManager:
    def __init__ (self):
        self.tasks = []
    
    def add_task(self, title):
        new_task = Task(title)
        task_id = random.randint(0,100)
        new_task.task_id = task_id 
        self.tasks.append(new_task)
        return new_task
    
    def show_tasks(self):
        return self.tasks
    
    def get_task(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                return task
        return None
    
    def get_status(self, task_id):
        for tasks in self.tasks:
            if task_id == tasks.task_id:
                return tasks.status
            
    def complete_tasks(self, task_id):
        task = self.get_task(task_id)

        if task is None:
            return f"Task with id {task_id} was not found."

        if task.status == "completed":
            return f"Task with id {task_id} is already completed."

        task.status = "completed"
        return f'Task with id {task_id} has been marked "completed": {task.title}'
    
    def delete_task(self, task_id):
        task = self.get_task(task_id)
        if task is not None:
            self.tasks.remove(task)
            return True
        return False


        

        




