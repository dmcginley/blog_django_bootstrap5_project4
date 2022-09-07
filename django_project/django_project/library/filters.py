
import django_filters


# import django_filters
from .models import *
from dataclasses import field


class PostFilter(django_filters.FilterSet):

    class Meta:
        models = Post
        fields = '__all__'
