from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_on']


class PostImage(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.post.title


class comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=False)
    commentor = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    created_on = models.DateTimeField(auto_now_add=True)
    content = models.TextField(default=None)

    class Meta:
        ordering = ['-created_on']
