from distutils.command.upload import upload
from email.policy import default
from django.db import models
from django.contrib.auth.models import User


# Create user profile here - e.g. profile pic, bio, location...
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(
        default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'
