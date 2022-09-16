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
from users_app.models import Profile
from users_app.forms import CommentForm


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'techblog_app/index.html', context)


# all the posts on the main page
class PostListView(ListView):
    model = Post
    template_name = 'techblog_app/index.html'

    context_object_name = 'posts'
    ordering = ['-date_posted']  # date posted in reverse order
    paginate_by = 5


class UserPostListView(ListView):
    model = Post
    template_name = 'techblog_app/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

    # insert an extra variable into the context for this list view
    def get_context_data(self, **kwargs):
        context = super(UserPostListView, self).get_context_data(**kwargs)
        username = self.kwargs.get('username')
        print(f"loading user? {username}")

        user = User.objects.filter(username=username).first()

        print(user)
        context.update({
            'user': user
        })
        return context


# ------------------------------
#    the 4 post views: DetailVie, Create, Update, Delete.
# ------------------------------
class PostDetailView(DetailView):
    model = Post


# to create a post
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'techblog_app/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


# update a post
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'techblog_app/user_posts_update.html'

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
    # the 4 comment views: DetailView Create, Update, Delete.
# ------------------------------
class CommentDetailView(DetailView):
    model = Comment


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'techblog_app/comment_form.html'

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('post-detail', kwargs={'pk': self.object.post.pk})


class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    fields = ['title', 'content']
    template_name = 'techblog_app/user_comments_update.html'

    def form_valid(self, form):

        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        comment = self.get_object()
        if self.request.user == comment.author:
            return True
        return False

    def get_success_url(self):
        print("updating ", self.object.post.pk, self.object.pk)
        return reverse('post-detail', kwargs={'pk': self.object.post.pk})


# delete a post, and goes back to homepage
class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment

    def test_func(self):
        comment = self.get_object()
        if self.request.user == comment.author:
            return True
        return False

    def get_success_url(self):
        print(
            f"deleting comment {self.object.pk} from post {self.object.post.pk}")
        return reverse('post-detail', kwargs={'pk': self.object.post.pk})


# ------------------------------
#   the about and page not found
# ------------------------------
def about(request):

    return render(request, 'techblog_app/about.html', {'title': 'About'})


# ------------------------------
#   error views: 400, 403, 404, & 500
# ------------------------------
def bad_request(request, *args, **argv):
    return render(request, 'techblog_app/error400.html', status=400)


def access_denied(request,  *args, **argv):
    return render(request, 'techblog_app/error403.html', status=403)


def page_not_found_view(request, *args, **argv):
    return render(request, 'techblog_app/error404.html', status=404)


def handler500(request,  *args, **argv):
    return render(request, 'techblog_app/error500.html', status=500)
