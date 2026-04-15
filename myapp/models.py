from django.db import models

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    def progress(self):
        total = self.task_set.all().count()
        done_tasks = self.task_set.filter(done = True).count()
        
        if total and done_tasks:
                progress = (done_tasks / total) * 100
        
        else:
            progress = 0
        return int(progress)

    
    
    def __str__(self):
        return self.name

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete= models.CASCADE)
    done = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
    
    
    

    