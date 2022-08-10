import imp
from xml.etree.ElementTree import Comment
from django.contrib import admin
from .models import Post, Comment


# models
# add post to django admin page
admin.site.register(Post)
admin.site.register(Comment)
