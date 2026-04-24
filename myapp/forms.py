from django import forms
from .models import Project


class CreateNewTask(forms.Form): #related with the model 'Task'
    
    title = forms.CharField(label = 'Title', max_length=200)
    description = forms.CharField(widget= forms.Textarea, label="Description", required=False)
    


class CreateNewProject(forms.Form): #related with the model 'Project'
    name = forms.CharField(label='Project Name', max_length=200)
    description = forms.CharField(widget=forms.Textarea, label="description", required=False)
    