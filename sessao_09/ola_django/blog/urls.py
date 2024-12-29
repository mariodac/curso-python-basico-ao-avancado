from django.contrib import admin
from django.urls import path
from . import views

# blog/
urlpatterns = [
    path("", views.index), 
    path("exemplo/", views.exemplo),
]
