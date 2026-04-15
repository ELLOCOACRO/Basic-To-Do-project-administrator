from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name= 'index'),
    path('about/', views.about, name = 'about'),
    path('projects/', views.projects, name = 'projects'),
    path('projects/<int:id>/', views.project_tasks, name = 'project_tasks'),
    path('/add_task/<int:id>/', views.addTask, name = 'add_task'),
    path('tasks/', views.task, name = 'tasks'),
    path('create_new_project/', views.create_project, name = 'create_project'),
    

]