from django.urls import path
from blog.views import (
    page,
    post,
    PostListView,
    CreatedByListView,
    CategoryListView,
    TagListView,
    SearchListView,
)

app_name = "blog"

urlpatterns = [
    path("", PostListView.as_view(), name="index"),
    path("post/<slug:slug>/", post, name="post"),
    path("page/", page, name="single_page"),
    path("page/<slug:slug>/", page, name="page"),
    path("created_by/<int:author_id>/", CreatedByListView.as_view(), name="created_by"),
    path("category/<slug:slug>/", CategoryListView.as_view(), name="category"),
    path("tag/<slug:slug>/", TagListView.as_view(), name="tag"),
    path("search/", SearchListView.as_view(), name="search"),
]
