from typing import Any
from django.http import HttpRequest, Http404
from django.shortcuts import render
from blog.data import get_posts
from random import shuffle


# Create your views here.
def index(request):
    data = get_posts()
    shuffle(data)
    content = {
        "title": "Todos os posts",
        "posts": data,
    }
    return render(request, "blog/blog.html", content)


# foi criado o namespace, onde é criado uma pasta com o mesmo nome do app (blog/templates/blog/*), assim evita a colisão de nomes de arquivos iguais em outros apps
def album(request):
    data = get_posts()
    for post in data:
        post["title"] = ' '.join(post["title"].split(" ")[0:2])
        post["photo"] = f"https://picsum.photos/320?r={post['id']}"
    shuffle(data)
    content = {"text": "Bem-vindo ao álbum!", "title": "Página álbum do blog", "posts": data,}
    return render(request, "blog/album.html", content)


def post(request: HttpRequest, post_id):
    found_post: dict[str, Any] | None = None
    data = get_posts()
    for post_item in data:
        if post_item["id"] == post_id:
            found_post = post_item
            break
    print(found_post)
    if found_post is None:
        raise Http404("Post não encontrado")
    content = {"title": f'Post {found_post["title"]}', "post": found_post}
    return render(request, "blog/post.html", content)
