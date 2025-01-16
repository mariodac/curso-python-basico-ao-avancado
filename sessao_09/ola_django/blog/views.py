from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"blog/blog.html")


# foi criado o namespace, onde é criado uma pasta com o mesmo nome do app (blog/templates/blog/*), assim evita a colisão de nomes de arquivos iguais em outros apps
def exemplo(request):
    return render(request, "blog/exemplo.html")