from django.conf import settings
from django.db import models
from django.utils import timezone

class Paper():
    id = models.AutoField(primary_key=True)

    
class Author():
    pass


class Comment():
    id = models.AutoField(primary_key=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.description