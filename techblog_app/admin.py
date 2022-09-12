# import imp
# from xml.etree.ElementTree import Comment
from django.contrib import admin
from .models import Post, Comment
# from users_app.models import Profile
# from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass
