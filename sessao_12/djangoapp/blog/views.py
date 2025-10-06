from typing import Any
from django.db.models.query import QuerySet
from django.http import Http404, HttpRequest
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.db.models import Q
from blog.models import Post, Page, User
from django.views.generic import ListView
PER_PAGE = 9


class PostListView(ListView):
    model = Post
    template_name = "blog/pages/index.html"
    context_object_name = "posts"
    ordering = "-pk",
    paginate_by = PER_PAGE
    queryset = Post.objects.get_published()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({"page_title": "Home - "})
        return context


class CreatedByListView(PostListView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._tmp_context = {}
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self._tmp_context["user"]
        user_fullname = user.username
        if user.first_name:
            user_fullname = f"{user.first_name} {user.last_name}"
        context.update({
            "page_title": f"Posts de {user_fullname} - ",
        })
        return context
    
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(created_by__pk=self._tmp_context["author_id"])
        return queryset

    
    def get(self, request, *args, **kwargs):
        author_pk = self.kwargs.get("author_id")
        user = User.objects.filter(pk=author_pk).first()

        if user is None:
            raise Http404()
        
        self._tmp_context.update({
            "author_id": author_pk,
            "user": user,
        })
        return super().get(request, *args, **kwargs)


class CategoryListView(PostListView):
    allow_empty = False

    def get_queryset(self) -> QuerySet[Any]:
        return super().get_queryset().filter(category__slug=self.kwargs.get("slug"))
    
    def get_context_data(self, **kwargs):   
        context = super().get_context_data(**kwargs)
        # metodo 1
        context.update({
            "page_title": f"{context['posts'][0].category.name} - Categoria - ",
        })

        # metodo 2
        # context.update({
        #     "page_title": f"{self.object_list[0].category.name} - Categoria - ", #type: ignore
        # })
        
        return context
    

class TagListView(PostListView):
    allow_empty = False

    def get_queryset(self) -> QuerySet[Any]:
        return super().get_queryset().filter(tags__slug=self.kwargs.get("slug"))
    
    def get_context_data(self, **kwargs):   
        context = super().get_context_data(**kwargs)
        # metodo 1
        context.update({
            "page_title": f"{context['posts'][0].tags.first().name} - Tag - ",
        })

        # metodo 2
        # context.update({
        #     "page_title": f"{self.object_list[0].tags.first().name} - Tag - ", #type: ignore
        # })
        
        return context
    

class SearchListView(PostListView):
    def __init__(self, *args, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self._search_value = ""

    def setup(self, request: HttpRequest, *args: Any, **kwargs: Any) -> None:
        self._search_value = request.GET.get("search", "").strip()
        return super().setup(request, *args, **kwargs)

    def get_queryset(self) -> QuerySet[Any]:
        search_value = self.request.GET.get("search", "").strip()
        return super().get_queryset().filter(
            Q(title__icontains=search_value)
            | Q(excerpt__icontains=search_value)
            | Q(content__icontains=search_value)
        )
    
    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        search_value = self.request.GET.get("search", "").strip()
        context.update({
            "search_value": search_value,
            "page_title": f"{search_value[:20]} - Busca - ",
        })
        return context
    
    def get(self, request, *args: Any, **kwargs: Any):
        if not self._search_value:
            return redirect("blog:index")
        return super().get(request, *args, **kwargs)

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
