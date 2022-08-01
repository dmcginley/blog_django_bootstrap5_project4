import imp
from urllib import request
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# from django_project import users
from .models import Post


# Create your views here.


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'library/index.html', context)


# list views


class PostListView(ListView):
    model = Post
    template_name = 'library/index.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']  # date posted in reverse order
    paginate_by = 4


# for user profile page


class UserPostListView(ListView):
    model = Post
    template_name = 'library/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 4


# query user from href link

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

# detail view of a post


class PostDetailView(DetailView):
    model = Post
    # template_name = 'library/index.html'
    # context_object_name = 'posts'
    # ordering = ['-date_posted']


# to create a post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


# update a post


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


# delete a post, and goes back to homepage


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'library/about.html', {'title': 'About'})


# def profile(request):
#     return render(request, 'library/profile.html', {'title': 'Profile'})
