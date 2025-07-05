from django.shortcuts import render
from django.core.paginator import Paginator

posts = list(range(1000))
paginator = Paginator(posts, 9)


def index(request):
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "blog/pages/index.html", {"page_obj": page_obj})


def page(request):
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "blog/pages/page.html", {})


def post(request):
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "blog/pages/post.html", {})
