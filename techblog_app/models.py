from email.policy import default
import imp
import django
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from users_app.models import Profile
from datetime import datetime
from django_quill.fields import QuillField


class DateTimeWithoutTZField(models.DateTimeField):
    def db_type(self, connection):
        return 'timestamp'


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = QuillField(blank=True, null=True)
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
    title = models.CharField(max_length=100)
    content = QuillField(blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-date_posted',)

    def __str__(self):
        return f"comment by {self.author}"

    def get_absolute_url(self):
        return reverse('comment-detail', kwargs={'pk': self.pk})
