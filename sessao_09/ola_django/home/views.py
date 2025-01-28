from django.shortcuts import render
from blog.data import get_posts
from random import shuffle

# Create your views here.

def index(request):
    data = get_posts()
    shuffle(data)
    context = {
            'text': 'Olá Mundo!',
            'title': 'Bem-vindo',
            'posts': data[:5],
        }
    return render(
        request, 
        'home/home.html',
        context,
    )