from csv import list_dialects
from pyexpat import model
from statistics import mode
from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from django.utils.html import format_html
from techblog_app.models import Comment, Post
from .models import Profile
from users_app import models

# admin profile


class ProfileAdmin(admin.ModelAdmin):
    def avatar(self, obj):
        return format_html('<img src="{}" style="max-width:100px;\
             max-height:200px"/>'.format(obj.image.url))

    list_display = ['user', 'avatar', ]


admin.site.register(Profile, ProfileAdmin)


# Unregister the provided model admin, and Register out own model admin
# from
# https://realpython.com/manage-users-in-django-admin/?utm_source=pocket_mylist


# admin user +profile field
admin.site.unregister(User)


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, )

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)

    list_display = ['username', 'email', 'is_staff', 'is_active']
    readonly_fields = [
        'date_joined',
        'last_login'
    ]


# ------------------------
# admin area posts
# ------------------------
admin.site.unregister(Post)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    search_fields = ('title', 'content')
    list_display = ['title', 'author', 'date_posted']
    list_filter = ('author', 'date_posted')

    readonly_fields = [
        'date_posted'
    ]


def get_readonly_fields(self, request, obj=None):
    return ('date_posted', 'author',)


# ------------------------
# admin area comments
# ------------------------
admin.site.unregister(Comment)


@admin.register(Comment)
class PostAdmin(admin.ModelAdmin):
    search_fields = ('title', 'content')
    list_display = ['title', 'author', 'date_posted']
    list_filter = ('author', 'date_posted')

    readonly_fields = [
        'date_posted'
    ]

    def get_readonly_fields(self, request, obj=None):
        return ('post', 'date_posted', 'author', )
