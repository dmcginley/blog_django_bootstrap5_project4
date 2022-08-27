import imp
from multiprocessing import context
from urllib import request
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.shortcuts import render

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Comment
from users.models import Profile
# from .filters import PostFilter
from users.forms import CommentForm
# from django.core.paginator import Paginator


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'library/index.html', context)


# all the posts on the main page
class PostListView(ListView):
    model = Post
    template_name = 'library/index.html'

    context_object_name = 'posts'
    ordering = ['-date_posted']  # date posted in reverse order
    paginate_by = 8


class UserPostListView(ListView):
    model = Post
    template_name = 'library/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 8

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


# my user profile page
    # TODO: fix my user profile page, just viewable to  me
    # TODO: add a redirect for this page, as it's one I shouldn't be looking for

# class UserProfilePostView(LoginRequiredMixin, UserPassesTestMixin, ListView):
class UserProfilePostView(LoginRequiredMixin, ListView):
    # TODO:  login_required not working
    model = Post
    template_name = 'library/profile.html'
    context_object_name = 'posts'
    paginate_by = 8

    def test_func(self):

        profile = Profile.user
        if self.request.user == profile:
            return True
        return False

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


# ------------------------------
#    the 4 post views: Detail, Create, Update, Delete.
# ------------------------------
class PostDetailView(DetailView):
    model = Post


# to create a post
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'library/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


# update a post

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'library/user_posts_update.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


# ------------------------------
    # the 3 comment views: Create, Update, Delete.
# ------------------------------
# TODO: should I have DetailView for comments
class CommentDetailView(DetailView):
    model = Comment
# ------------------------------


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'library/comment_form.html'

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('post-detail', kwargs={'pk': self.object.post.pk})


class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    fields = ['title', 'content']
    template_name = 'library/user_comments_update.html'
    # success_url = '/'

    def form_valid(self, form):

        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        comment = self.get_object()
        if self.request.user == comment.author:
            return True
        return False


# delete a post, and goes back to homepage


# BUG: to fix: delete comment not set up properly

class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    success_url = '/'
    # template_name = 'library/comment_confirm_delete.html'

    def test_func(self):
        comment = self.get_object()
        if self.request.user == comment.author:
            return True
        return False


# ------------------------------
#   the about and page not found
# ------------------------------
def about(request):

    return render(request, 'library/about.html', {'title': 'About'})


def page_not_found_view(request, exception):
    return render(request, 'library/error404.html', status=404)

# TODO : add functions for 403, 400, 500 error views
