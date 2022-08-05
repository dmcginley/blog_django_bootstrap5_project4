from django.urls import path
from .views import (
    PostListView, PostDetailView,
    PostCreateView, PostUpdateView,
    PostDeleteView, UserPostListView,
    UserProfilePostView
)
from . import views

# urlpatterns = [
#     path('', views.home, name='library-home'),
#     path('about/', views.about, name='library-about'),
# ]

urlpatterns = [
    path('', PostListView.as_view(), name='library-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='library-about'),
    path('profile/<str:username>/',
         UserProfilePostView.as_view(), name='profile'),

]
