from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Project

# Create your views here.
"""_summary
Métodos para renderizar
"""
def inicio(request):
    return HttpResponse("Hola Django!!")

def landing(request):
    return render(request,'index.html')

"""
Métodos de Project
"""
def listProjects(request):
    projects = Project.objects.all()
    return render(request,'projects/list.html',{
        "projects":projects
    }) 

def showFormCreateProject(request):
    return render(request,'projects/create.html')

def storeProject(request):
    project = Project.objects.create(
        name = request.POST["name"],
        description = request.POST["description"]
    )
    project.save()
    return redirect('projects.list')

def showFormEditProject(request,project_id):
    project = get_object_or_404(Project,id=project_id)
    return render(request,'projects/edit.html',{
        'project': project
    })

def updateProject(request,project_id):
    project = get_object_or_404(Project,id=project_id)

    project.name = request.POST["name"]
    project.description = request.POST["description"]

    project.save()

    return redirect('projects.list')
