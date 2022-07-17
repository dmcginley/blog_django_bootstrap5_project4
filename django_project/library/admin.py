import imp
from django.contrib import admin
from .models import Post


# models
# add post to django admin page
admin.site.register(Post)
