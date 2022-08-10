from turtle import title
import django
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from users.models import Profile


# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


# the comment section


class Comment(models.Model):
    post = models.ForeignKey(
        Post, related_name="comments", on_delete=models.CASCADE)

    # image = object.author.profile.image.url

    name = models.CharField(max_length=100)
    body = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)
