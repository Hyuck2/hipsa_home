from django.contrib import admin
from .models import Meeting, Topic, Comment, Category
# Register your models here.

admin.site.register(Meeting)
admin.site.register(Topic)
admin.site.register(Comment)
admin.site.register(Category)