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
    
    if request.method == "GET":
        projects = Project.objects.values()
        return render(request, 'project/projects.html', {
            'projects' : projects,
            'breadcrumb': breadcrumb,
        })
        
    elif request.POST['DELETE']:
            
            id = int(request.POST['DELETE'])
            project = get_object_or_404(Project, id=id)
            project.delete()
            return redirect('projects')



#Create project view, it return a seccion with a form for create new projects, and
#at the same time procces the form request 
def create_project(request):
    
    breadcrumb = [("home", '/'),
                  ("Create project", None),
                  ]
    
    if request.method == "GET":
        
        return render(request, 'project/create_project.html', {
            'projectForm' : CreateNewProject(),
            'breadcrumb' : breadcrumb,
        })
    
    else:
        Project.objects.create(name = request.POST['name'])
        return redirect('projects')
    
    
    
def project_tasks(request, id):
    project = get_object_or_404(Project, id = id)
    tasks = project.task_set.filter(project = project)
    tasks_done = tasks.filter(done = True)
    tasks_pendience = tasks.filter(done = False)
    
    breadcrumb = [("home", "/"),
                   ("projects", "/projects/"),
                   (project.name, None),
                   ]
    
    
    if request.method == "GET":
        return render(request, 'project/project_tasks.html', {
            'project' : project,
            'tasks' : tasks,
            'tasks_done' : tasks_done,
            'tasks_pendience' : tasks_pendience,
            'breadcrumb' : breadcrumb,
        })
    
    elif request.POST.get('DELETE'):
        id = int(request.POST['DELETE'])
        task = get_object_or_404(Task, id = id)
        task.delete()
                
    elif request.POST.get('PUT'):
        id = int(request.POST['PUT'])
        task = get_object_or_404(Task, id = id)
        task.done = not task.done
        task.save()
            
            
    return redirect('project_tasks', project.id)
            
            
  
   


def addTask(request, id):
    
    form = CreateNewTask()
    project = get_object_or_404(Project, id = id)
    breadcrumb = [("home", "/"),
                   ("projects", "/projects/"),
                   (project.name, f'/projects/{project.id}'),
                   ('AddTask', None),
                   ]
    
    if request.method == "POST":
        
        title = request.POST.get('title')
        description = request.POST.get('description')
        project.task_set.create(title = title, description = description)
        
        
    
    return render(request, 'task/add.html', {
            'form': form,
            'project' : project,
            'breadcrumb' : breadcrumb,
            
        })

#############################
###PROJECT VIEWS ENDS HERE###
#############################



def task(request):
    tasks = Task.objects.all()

    return render(request, 'task/tasks.html', {
        'tasks' : tasks
    })




    
        
    
    
    
    
    

