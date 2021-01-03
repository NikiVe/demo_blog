from django.db import models
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(UserModel, null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_picture = models.ImageField(blank=True, upload_to='profile_images/')
    fb_url = models.URLField(blank=True)
    twitter_url = models.URLField(blank=True)
    instagram = models.URLField(blank=True)

    def __str__(self):
        return f'{self.user}'
