from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inicio/',views.inicio),
    path('landing',views.landing),
    path('projects/',views.listProjects)
]