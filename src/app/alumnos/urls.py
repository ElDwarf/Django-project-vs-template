from django.contrib import admin
from django.urls import path, include
from .views import add_alumno, get_alumnos, alumno

urlpatterns = [
    path('', get_alumnos),
    path('addalumno/', add_alumno),
    path('alumno/', alumno),
]
