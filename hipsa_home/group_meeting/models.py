from django.conf import settings
from django.db import models
from django.utils import timezone

class Meeting(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.CharField(max_length=200)
    attendent = models.CharField(max_length=200)
    place = models.CharField(max_length=200)
    topics = models.CharField(max_length=200)

class Topic(models.Model):
    #parent = models.CharField(max_length=200)
    parent = models.ForeignKey(Category.id, on_delete=models.CASCADE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.CharField(max_length=200)
    close_date = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    status = models.CharField(max_length=200)

class Comment(models.Model):
    #topic_id = models.CharField(max_length=200)
    topic_id = models.ForeignKey(Topic.id, on_delete=models.CASCADE)
    #parent = models.CharField(max_length=200)
    parent = models.ForeignKey(Comment.id, on_delete=models.CASCADE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.CharField(max_length=200)
    description = models.CharField(max_length=200)

class Category(models.Model):
    name = models.CharField(max_length=200)