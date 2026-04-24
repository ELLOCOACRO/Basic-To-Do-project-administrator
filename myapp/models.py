from django.db import models
from django.db.models import QuerySet
# Create your models here.


class Project(models.Model):
    """
    The object Project is the main object, has only 2 properties: name, description and progress
    and has many methods like get_tasks and get_completed_tasks.
    
    it has a relationship one to many  (1:N) with the object 'Task'
    """
    #Properties
    name = models.CharField(max_length=200)
    description = models.TextField()
    
    

    @property
    def progress(self) -> int: 
        """
        get all tasks and all completed_tasks and returns
        the progress of the project in base of (a / b) * 100.
        
        If the're no tasks or completed_tasks return 0, otherwise return the progress 
    
        """
        
        total = self.tasks.all().count()
        completed_tasks = self.tasks.filter(done = True).count()
        
        
        if total:
            progress = (completed_tasks / total) * 100
        
        else:
            return 0
            
        return int(progress)
    
    
    def get_tasks(self) -> QuerySet: 
        """
        return a querydict with all tasks of the project
        """
        return self.tasks.all()
    
    
    def get_completed_tasks(self) -> QuerySet: 
        """
        return a queryset with all complete_tasks of the project
        if task is done return task otherwise return None
        
        """
        
        completed_tasks = self.tasks.filter(done = True)
        return completed_tasks
            
            
    def get_uncompleted_tasks(self)->QuerySet:
        
        """
        return a queryset with all uncompleted tasks of the project
        if the task isnt done return task
        otherwise return None
        """
        uncompleted_tasks = self.tasks.filter(done = False)
        return uncompleted_tasks
        
        
        

    def __str__(self):
        return self.name
    
    
    
    
class Task(models.Model):
    """
    Object Task. 
    This objects has a relationship many to one (N:1) with the object 'Project'
    and have attrs like title, desc, project etc.., with methods like set_done and more.
    """

    
    title = models.CharField(max_length=200)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete= models.CASCADE, related_name="tasks")
    done = models.BooleanField(default=False)
    
 
    
    def set_done(self): 
        """
        update 'done' propertie to True,
        if the task is done update it, otherwise return none
        """
        
        
        if not self.done:
            self.done = True
            self.save()
        
        else:
            return None

    
    def is_done(self):
        """
        return True or false on wether the task is done
        """
    
        if self.done:
            return True
        
        else:
            return None
            
 
    def __str__(self):
        return self.title
    
    
    

    