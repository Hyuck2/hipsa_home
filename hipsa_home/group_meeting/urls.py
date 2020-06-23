from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('list/', views.meeting_list, name = 'list'),
    path('list/<int:meeting_id>/', views.list_detail, name='list_detail'),
]