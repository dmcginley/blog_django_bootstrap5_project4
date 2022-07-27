from django.shortcuts import render
from .models import Post

# Create your views here.


def home(request):
    context = {
        'posts': Post.objects.all
    }
    return render(request, 'library/index.html', context)


def about(request):
    return render(request, 'library/about.html', {'title': 'About'})


def profile(request):
    return render(request, 'library/profile.html', {'title': 'Profile'})
