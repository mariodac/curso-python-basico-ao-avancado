from django.contrib import admin
from django.urls import path
from . import views

app_name = "blog"

# blog/
# Django URLs
# https://docs.djangoproject.com/en/5.1/topics/http/urls/
urlpatterns = [
    path("", views.index, name="home"), 
    path("post/<int:id>", views.post, name="post"), 
    path("exemplo/", views.exemplo, name="exemplo"),
]
