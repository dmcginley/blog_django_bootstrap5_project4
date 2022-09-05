import imp
from xml.etree.ElementTree import Comment
from django.contrib import admin
from .models import Post, Comment
from users.models import Profile


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'date_posted']
    search_fields = ('title', 'content')

    list_filter = ('author', 'date_posted')
    readonly_fields = [
        'title',
        'content',
        'author',
        'date_posted'
    ]


class CommentAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'date_posted']
    search_fields = ('title', 'content')
    list_filter = ('author', 'date_posted')


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
