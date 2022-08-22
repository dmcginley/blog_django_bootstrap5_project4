from distutils.command.upload import upload
from email.policy import default
from django.db import models
from django.contrib.auth.models import User
# from PIL import Image

# TODO: pillow not importing properly
# from PIL import Image, ImageDraw, ImageFilter
from PIL import Image, ImageDraw, ImageFilter


# the original class
# -----------------------------------------------
# Create user profile here - e.g. profile pic, bio, location...
# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     image = models.ImageField(
#         default='default.jpg', upload_to='profile_pics')

#     def __str__(self):
#         return f'{self.user.username} Profile'

#     def save(self, *args, **kwargs):
#         super().save(*args, **kwargs)

#         img = Image.open(self.image.path)

#         if img.height > 320 or img.width > 320:
#             output_size = (320, 320)
#             img.thumbnail(output_size)
#             img.save(self.image.path)
# -----------------------------------------------


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(
        default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)
        width, height = img.size  # Get dimensions

        if width > 300 and height > 300:
            # keep ratio but shrink down
            img.thumbnail((width, height))

        # check which one is smaller
        if height < width:
            # make square by cutting off equal amounts left and right
            left = (width - height) / 2
            right = (width + height) / 2
            top = 0
            bottom = height
            img = img.crop((left, top, right, bottom))

        elif width < height:
            # make square by cutting off bottom
            left = 0
            right = width
            top = 0
            bottom = width
            img = img.crop((left, top, right, bottom))

        if width > 300 and height > 300:
            img.thumbnail((300, 300))

        img.save(self.image.path)


# -----------------------------------------------

        # TODO: if not square, crop to square
        # TODO:  add crop to image upload

# class CustomUser(AbstractBaseUser, PermissionsMixin):
#     # User model fields, etc
#     image = models.ImageField(default='default.jpg',upload_to='profile_pics')

#     def save(self, *args, **kwargs):
#         super().save()
#         img = Image.open(self.image.path)
#         width, height = img.size  # Get dimensions

#         if width > 300 and height > 300:
#             # keep ratio but shrink down
#             img.thumbnail((width, height))

#         # check which one is smaller
#         if height < width:
#             # make square by cutting off equal amounts left and right
#             left = (width - height) / 2
#             right = (width + height) / 2
#             top = 0
#             bottom = height
#             img = img.crop((left, top, right, bottom))

#         elif width < height:
#             # make square by cutting off bottom
#             left = 0
#             right = width
#             top = 0
#             bottom = width
#             img = img.crop((left, top, right, bottom))

#         if width > 300 and height > 300:
#             img.thumbnail((300, 300))

#         img.save(self.image.path)
