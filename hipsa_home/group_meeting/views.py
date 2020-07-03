from django.shortcuts import render
from .models import Meeting, Topic, Comment, Category
from django.http import HttpResponse
from datetime import timedelta

def home(request):
    today = Meeting.objects.order_by('-date')[0]
    comments = Comment.objects.filter(updated__range=(today.date-timedelta(days=7),today.date+timedelta(days=1)))
    return render(
        request,
        'group_meeting/home.html',
        {
            'today':today,
            'comments':comments,
        }
    )

def meeting_list(request):
    meetings = Meeting.objects.order_by('date')
    return render(
        request, 
        'group_meeting/list.html',
        {
            'meetings':meetings,
        }
    )

def list_detail(request, meeting_id):
    meeting = Meeting.objects.get(id=meeting_id)
    comments = Comment.objects.filter(updated__range=(meeting.date-timedelta(days=7),meeting.date+timedelta(days=1)))    
    return render(
        request,
        'group_meeting/list_detail.html', 
        {
            'meeting':meeting,
            'comments':comments,
        }
    )
