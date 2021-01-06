from django.contrib.auth import get_user_model
from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField

UserModel = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(editable=False)
    author = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    category = models.CharField(max_length=250)
    snippet = models.CharField(max_length=250)
    content = RichTextField(blank=True, null=True)
    # content = models.TextField()
    image = models.ImageField(blank=True, upload_to='images/')
    likes = models.ManyToManyField(UserModel, related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return f'{self.title} | {self.author}'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)


class Comment(models.Model):
    text = models.TextField(blank=False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)


