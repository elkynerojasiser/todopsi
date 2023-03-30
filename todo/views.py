from django.shortcuts import render
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
