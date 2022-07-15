from django.shortcuts import render
from .models import Post

# Create your views here.


# posts = [
#     {
#         'title': 'master',
#         'author': 'cat',
#         'age': '24',
#         'year': '12 Feb 2019',
#         'content': 'lorem dolor sit amet consectetur adipisicing elit. Explicabo suscipit qui sit autem id porro repellat soluta voluptat'
#     },
#     {
#         'title': 'shop',
#         'author': 'cat',
#         'age': '18',
#         'year': '23 Sep 2009',
#         'content': 'lorem dolor sit amet consectetur adipisicing elit.olor sit amet consectetur adipisicing elit Explicabo suscipit qui sit autem id porro repellat soluta voluptat'
#     }
# ]


def home(request):
    context = {
        'posts': Post.objects.all
    }
    return render(request, 'library/index.html', context)


def about(request):
    return render(request, 'library/about.html', {'title': 'About'})
