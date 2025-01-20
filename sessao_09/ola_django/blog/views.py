from django.shortcuts import render
from blog.data import get_posts, search_by_id

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

def post(request, id):
    data = get_posts()
    index = search_by_id(data, id)
    content = {
        # 'title' : f'Post {id}',
        'title' : f'Post {data[index]["title"]}',
        'posts' : data
    }
    return render(
        request,
        "blog/blog.html",
        content
    )