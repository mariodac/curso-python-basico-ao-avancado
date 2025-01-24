from typing import Any
from django.http import HttpRequest
from django.shortcuts import render
from blog.data import get_posts

# Create your views here.
def index(request):
    data = get_posts()
    content = {
        'title' : 'Todos os posts',
        'posts' : data
    }
    return render(
        request,
        "blog/blog.html",
        content
    )


# foi criado o namespace, onde é criado uma pasta com o mesmo nome do app (blog/templates/blog/*), assim evita a colisão de nomes de arquivos iguais em outros apps
def exemplo(request):
    content = {
        'text': 'Bem-vindo ao exemplo!',
        'title': 'Página exemplo do blog'
    }
    return render(
        request, 
        "blog/exemplo.html",
        content
    )

def post(request: HttpRequest, post_id):
    found_post: dict[str, Any] | None = None
    data = get_posts()
    for post_item in data:
        if post_item['id'] == post_id:
            found_post = post_item
            break
    print(found_post)
    if found_post is None:
        raise Exception("Post não encontrado")
    content = {
        # 'title' : f'Post {id}',
        'title' : f'Post {found_post["title"]}',
        'post' : found_post
    }
    return render(
        request,
        "blog/post.html",
        content
    )