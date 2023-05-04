from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Project
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

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
@login_required
def listProjects(request):
    projects = Project.objects.all()
    return render(request,'projects/list.html',{
        "projects":projects
    }) 

@login_required
def showFormCreateProject(request):
    return render(request,'projects/create.html')

@login_required
def storeProject(request):
    project = Project.objects.create(
        name = request.POST["name"],
        description = request.POST["description"]
    )
    project.save()
    return redirect('projects.list')

@login_required
def showFormEditProject(request,project_id):
    project = get_object_or_404(Project,id=project_id)
    return render(request,'projects/edit.html',{
        'project': project
    })

@login_required
def updateProject(request,project_id):
    project = get_object_or_404(Project,id=project_id)

    project.name = request.POST["name"]
    project.description = request.POST["description"]

    project.save()

    return redirect('projects.list')

@login_required
def showConfirmDeleteProject(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    return render(request,'projects/delete.html',{
        'project' : project
    })

@login_required
def destroyProject(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    project.delete()
    return redirect('projects.list')

@login_required
def showDetailProject(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    return render(request, 'projects/detail.html',{
        'project': project
    })

def showSignupForm(request):
    return render(request,'users/signup-form.html')

def signup(request):
    if(request.POST['password'] == request.POST['password2']):
        try:
            user = User.objects.create_user(
                username=request.POST["username"],
                email=request.POST["email"],
                password=request.POST["password"],
                first_name=request.POST["first_name"],
                last_name=request.POST["last_name"]
            )
            user.save()
            login(request,user)
            return redirect('projects.list')
        except:
            return HttpResponse('something was wrong')
    else:
        return HttpResponse('The password fields don´t match')

def showLoginForm(request):
    return render(request,'users/login-form.html')

def startSession(request):
    user = authenticate(request=request,username=request.POST["username"],password=request.POST["password"])
    if(user is None):
        return redirect('login-form')
    else:
        login(request,user)
        return redirect('projects.list')

@login_required
def finishSession(request):
    logout(request)
    return redirect('home')