from django.db import models
from django.db.models.base import Model
from django.contrib.auth.models import User, Permission
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    liked = models.ManyToManyField(User, default=None, blank=True, related_name='likes')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')

    def __str__(self):
        return str(self.title)
    
    def num_likes(self):
        return self.liked.count()
    
LIKE_CHOICES = (
    ('Like', 'Like'),
    ('Unlike', 'Unlike'),
)

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES, default='Like', max_length=10)

    def __str__(self):
        return str(self.post)