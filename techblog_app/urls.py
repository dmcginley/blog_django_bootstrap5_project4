from xml.etree.ElementInclude import include
from django.urls import path
from .views import (
    PostListView, PostDetailView,
    PostCreateView, PostUpdateView,
    PostDeleteView, UserPostListView,
    CommentCreateView, CommentUpdateView,
    CommentDeleteView, CommentDetailView
)
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='techblog-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:post_id>/comment/<int:pk>/update',
         CommentUpdateView.as_view(), name='comment-update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:post_id>/comment/<int:pk>/delete',
         CommentDeleteView.as_view(), name='comment-delete'),
    path('about/', views.about, name='techblog-about'),
    path('post/<int:pk>/add-comment',
         CommentCreateView.as_view(), name='add-comment'),
]
