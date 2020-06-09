from django.contrib import admin
from django.urls import path
from group_meeting import views as group_meeting_views
from references import views as references_views
from blog import views as blog_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # group meeting urls
    path('group_meeting/', group_meeting_views.home, name = 'home'),
    
    # references urls
    path('references/', references_views.home, name = 'home'),

    # blog urls
    path('blog/', blog_views.home, name = 'home'),
]
