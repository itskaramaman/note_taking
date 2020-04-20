from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class Note(models.Model):
    title = models.CharField(max_length=180)
    content = models.TextField()
    date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
