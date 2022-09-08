from distutils.command.upload import upload
from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)

    image = models.ImageField(
        default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)

    #     img = Image.open(self.image.path)
    #     width, height = img.size  # Get dimensions

    #     if width > 300 and height > 300:
    #         # keep ratio but shrink image down
    #         img.thumbnail((width, height))

    #     if height < width:
    #         # make image square by cutting off equal amounts, left and right
    #         left = (width - height) / 2
    #         right = (width + height) / 2
    #         top = 0
    #         bottom = height
    #         img = img.crop((left, top, right, bottom))

    #     elif width < height:
    #         # make image square by cutting off the bottom
    #         left = 0
    #         right = width
    #         top = 0
    #         bottom = width
    #         img = img.crop((left, top, right, bottom))

    #     if width > 300 and height > 300:
    #         img.thumbnail((300, 300))

    #     img.save(self.image.path)
