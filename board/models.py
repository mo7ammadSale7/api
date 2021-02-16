from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class List(models.Model):
    title = models.CharField(max_length=100, null=True)
    member = models.ManyToManyField(User)

    def __str__(self):
        return self.title


class Card(models.Model):
    title = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True)
    list = models.ForeignKey(
        List, on_delete=models.CASCADE, related_name='cards')
    author = models.ForeignKey(User, null=True,  on_delete=models.CASCADE, related_name='cards_user')

    def __str__(self):
        return self.title


class Comment(models.Model):
    card = models.ForeignKey(
        Card, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='replies')

    def __str__(self):
        return self.body
