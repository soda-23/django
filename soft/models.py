from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Post(models.Model):
    author = models.ForeignKey(User, related_name='posts',on_delete=models.CASCADE)
    body = models.TextField()
    create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.author.username} -> {self.body}'
