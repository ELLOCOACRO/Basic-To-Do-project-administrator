from django.http import HttpResponse, JsonResponse, HttpRequest
from .models import Project, Task
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from .forms import CreateNewTask, CreateNewProject


# Create your views here.
def index(request):
    
    return render(request, 'index.html')

#About path: Just show a simple about page
def about(request):
    username = "erickmota"
    return render(request, 'about.html', {
        'username' : username,
    })


###############################
###PROJECT VIEWS START HERE####
################################

#Projects view, it return to a page that shows all projects
#ToDO: Make a function order automatically by the user selection
def projects(request):
    
    breadcrumb = [("home", '/'),
                  ("projects", None),
                  ]
    
    projects = Project.objects.all()

    if request.method == "GET":
        
        return render(request, 'project/projects.html', {
            'projects' : projects,
            'projectForm' : CreateNewProject(),
            'breadcrumb': breadcrumb,
        })
        
    else:
        if request.POST.get('DELETE'):
                
                id = int(request.POST['DELETE'])
                project = get_object_or_404(Project, id=id)
                project.delete()
                return redirect('projects')
            
        else:
            
            Project.objects.create(name = request.POST['name'], description = request.POST['description'])
            return redirect('projects')



 
 
def project_tasks(request, id):
    project = get_object_or_404(Project, id = id)

    
    breadcrumb = [("home", "/"),
                   ("projects", "/projects/"),
                   (project.name, None),
                   ]
    
    
    if request.method == "GET":
        TaskForm = CreateNewTask()
        return render(request, 'project/project_tasks.html', {
            'project' : project,
            'tasks' : project.tasks.all(),
            'completed_tasks' : project.get_completed_tasks(),
            'uncompleted_tasks': project.get_uncompleted_tasks(),
            'breadcrumb' : breadcrumb,
            'TaskForm': TaskForm,
        })
    
    else: 
        
        
      if request.POST.get('DELETE'):
        id = int(request.POST['DELETE'])
        task = get_object_or_404(Task, id = id)
        task.delete()
                
      elif request.POST.get('PUT'):
        task = get_object_or_404(Task, id = id)
        task.set_done()
        
        
      else:
          
          tTitle = request.POST.get('title')
          tDescription = request.POST.get('description')
          
          Task.objects.create(title = tTitle, description = tDescription, project = project)
            
      return redirect('project_tasks', project.id)
            
            
  
   


#############################
###PROJECT VIEWS ENDS HERE###
#############################







    
        
    
    
    
    
    

