from django.shortcuts import render
from blog.data import get_posts
from random import shuffle

# Create your views here.

def index(request):
    data = get_posts()
    for post in data:
        post["title"] = ' '.join(post["title"].split(" ")[0:2])
        post["photo"] = f"https://picsum.photos/320?r={post['id']}"
    shuffle(data)
    context = {
            'title': 'Bem-vindo',
            'posts': data[:10],
        }
    return render(
        request, 
        'home/home.html',
        context,
    )