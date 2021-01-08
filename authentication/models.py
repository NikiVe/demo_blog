from django.db import models
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE)
    bio = models.TextField(default='', blank=True)
    profile_picture = models.ImageField(null=True, blank=True, upload_to='profile_images/')
    fb_url = models.URLField(default='', blank=True)
    twitter_url = models.URLField(default='', blank=True)
    instagram = models.URLField(default='', blank=True)

    def __str__(self):
        return f'{self.user}'


class CustomProfile(models.Model):
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.name}'
