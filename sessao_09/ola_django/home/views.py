from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
            'text': 'Olá Mundo!',
            'title': 'Bem-vindo'
        }
    return render(
        request, 
        'home/home.html',
        context,
    )