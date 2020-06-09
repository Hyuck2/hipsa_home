from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('blog/', include('blog.urls')),
    path('group_meeting/', include('group_meeting.urls')),
    path('references/', include('references.urls')),
]
