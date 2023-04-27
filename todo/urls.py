from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inicio/',views.inicio),
    path('',views.landing,name="home"),
    path('projects/',views.listProjects,name="projects.list"),
    path('projects-create/',views.showFormCreateProject,name="projects.create"),
    path('projects-store',views.storeProject,name="projects.store"),
    path('projects-edit/<int:project_id>/',views.showFormEditProject,name="projects.edit"),
    path('projects-update/<int:project_id>',views.updateProject,name="projects.update"),
    path('projects-delete/<int:project_id>',views.showConfirmDeleteProject,name="projects.delete"),
    path('projects-destroy/<int:project_id>',views.destroyProject,name="projects.destroy"),
    path('projects-detail/<int:project_id>',views.showDetailProject,name="projects.detail"),
]