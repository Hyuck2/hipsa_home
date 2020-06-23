from django.conf import settings
from django.db import models
from django.utils import timezone

class Meeting(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='author')
    #date = models.CharField(max_length=200)
    date = models.DateField()
    attendent = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='attendent')
    place = models.CharField(max_length=200)
    topic = models.ManyToManyField('Topic')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.date)

    class Meta:
        pass

class Topic(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    owner = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='owner')
    start_date = models.DateField()
    close_date = models.DateField()
    name = models.CharField(max_length=200)
    # 
    status_list = (
        ('진행', '진행중인 안건'),
        ('종료', '종료된 안건'),
        ('보류', '보류된 안건'),
    )
    status = models.CharField(max_length=200, choices=status_list)
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        pass

class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    topic = models.ForeignKey('Topic', on_delete=models.CASCADE)
    parent = models.ForeignKey('Comment', on_delete=models.CASCADE, null=True, blank=True, default=0)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.description

    class Meta:
        pass

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name