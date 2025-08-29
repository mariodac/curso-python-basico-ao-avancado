from django.urls import path
from blog.views import category, created_by, index, page, post

app_name = "blog"

urlpatterns = [
    path("", index, name="index"),
    path("post/<slug:slug>/", post, name="post"),
    path("page/", page, name="single_page"),
    path("page/<slug:slug>/", page, name="page"),
    path("created_by/<int:author_id>/", created_by, name="created_by"),
    path("category/<slug:slug>/", category, name="category"),
]
