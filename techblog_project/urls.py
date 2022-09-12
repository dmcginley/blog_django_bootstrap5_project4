"""techblog_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django import template
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.urls import path, include
from users_app import views as user_views
import techblog_app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register', user_views.register, name='register'),
    path('edit_profile', user_views.edit_profile, name='edit_profile'),
    path('login', auth_views.LoginView.as_view(
        template_name='users_app/login.html'), name='login'),
    path('logout', auth_views.LogoutView.as_view(
        template_name='users_app/logout.html'), name='logout'),
    path('', include('techblog_app.urls')),

    path('summernote/', include('django_summernote.urls')),

]

# TODO: add references to error views - DEBUG must be False for custom views
#handler403 = 'techblog_app.views.access_denied'
handler404 = "techblog_app.views.page_not_found_view"
handler500 = "techblog_app.views.handler500"

#handler400 = ''


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
