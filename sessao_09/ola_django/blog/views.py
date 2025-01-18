from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'text' : 'Olá blog!',
        'title' : 'Página principal do blog'
    }
    return render(
        request,
        "blog/blog.html",
        context
    )


# foi criado o namespace, onde é criado uma pasta com o mesmo nome do app (blog/templates/blog/*), assim evita a colisão de nomes de arquivos iguais em outros apps
def exemplo(request):
    context = {
        'text': 'Olá exemplo!',
        'title': 'Página exemplo do blog'
    }
    return render(
        request, 
        "blog/exemplo.html",
        context
    )