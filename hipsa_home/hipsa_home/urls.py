from django.contrib import admin
from django.urls import path
from group_meeting import views as group_meeting_views
from references import views as references_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('group_meeting/', group_meeting_views.home, name = 'home'),
    path('references/', references_views.home, name = 'home'),
]
