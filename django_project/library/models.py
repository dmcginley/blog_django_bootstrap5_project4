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


# TODO: fix comments
# the comment section

class Comment(models.Model):
    post = models.ForeignKey(
        Post, related_name="comments", on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    date_posted = models.DateTimeField(default=timezone.now)
    # date_posted = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date_posted',)

    # def __str__(self):
    #     return '%s - %s' % (self.post.title, self.author)

    def __str__(self):
        return f"comment by {self.author}"
