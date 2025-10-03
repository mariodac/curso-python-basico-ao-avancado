from django.http import Http404
from django.shortcuts import render
from django.core.paginator import Paginator
from django.db.models import Q
from blog.models import Post, Page

PER_PAGE = 9


def index(request):
    # Function Based Views -> São funções
    # Class Based Views -> São classes (POO) https://docs.djangoproject.com/pt-br/4.2/ref/class-based-views/
    # se a view é simples, somente lê os dados e renderiza os templates, use function based views
    # se a view é mais complexa, use class based views

    # Obter dados do model
    # Esses dados são uma lista de objetos
    # Paginação
    # Renderizando um template
    # Manipulando o contexto

    posts = Post.objects.get_published()
    paginator = Paginator(posts, PER_PAGE)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(
        request,
        "blog/pages/index.html",
        {
            "page_obj": page_obj,
            "page_title": "Home - ",
        },
    )


def created_by(request, author_id):
    author = Post.objects.get_published().filter(created_by__pk=author_id).first()
    posts = Post.objects.get_published().filter(created_by__pk=author_id)
    paginator = Paginator(posts, PER_PAGE)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    if author is None:
        raise Http404()
    page_title = (
        f"Posts de {author.created_by.first_name} {author.created_by.last_name}"
    )
    return render(
        request,
        "blog/pages/index.html",
        {
            "page_obj": page_obj,
            "page_title": page_title,
        },
    )


def category(request, slug):
    posts = Post.objects.get_published().filter(category__slug=slug)
    paginator = Paginator(posts, PER_PAGE)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    if page_obj is None:
        raise Http404()
    page_title = f"Categoria - {page_obj[0].category.name} - "
    return render(
        request,
        "blog/pages/index.html",
        {
            "page_obj": page_obj,
            "page_title": page_title,
        },
    )


def tag(request, slug):
    posts = Post.objects.get_published().filter(tags__slug=slug)
    paginator = Paginator(posts, PER_PAGE)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    if page_obj is None:
        raise Http404()
    page_title = f"Tag - {page_obj[0].tags.first().name} - "
    return render(
        request,
        "blog/pages/index.html",
        {
            "page_obj": page_obj,
            "page_title": page_title,
        },
    )


def page(request, slug):
    page_obj = Page.objects.filter(is_published=True).filter(slug=slug).first()
    if page_obj is None:
        raise Http404()
    page_title = f"Page - {page_obj.title} - "
    return render(
        request,
        "blog/pages/page.html",
        {
            "page": page_obj,
            "page_title": page_title,
        },
    )


def post(request, slug):
    post_obj = Post.objects.get_published().filter(slug=slug).first()
    if post_obj is None:
        raise Http404()
    page_title = f"Post - {post_obj.title} - "
    return render(
        request,
        "blog/pages/post.html",
        {
            "post": post_obj,
            "page_title": page_title,
        },
    )


def search(request):
    search_value = request.GET.get("search", "").strip()
    # filter(title__icontains=search_value, body__icontains=search_value) a virgula funciona como o AND
    # filter(Q(title__icontains=search_value) | Q(excerpt__icontains=search_value) | Q(content__icontains=search_value)) o Q permite utilizar o operador | que funciona como OR
    posts = Post.objects.get_published().filter(
        Q(title__icontains=search_value)
        | Q(excerpt__icontains=search_value)
        | Q(content__icontains=search_value)
    )
    paginator = Paginator(posts, PER_PAGE)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    if page_obj is None:
        raise Http404()
    page_title = f"Busca - {search_value[:20]} - "
    return render(
        request,
        "blog/pages/index.html",
        {
            "page_obj": page_obj,
            "search_value": search_value,
            "page_title": page_title,
        },
    )
