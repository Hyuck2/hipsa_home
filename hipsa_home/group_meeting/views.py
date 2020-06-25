from django.shortcuts import render
from .models import Meeting, Topic, Comment, Category
from django.http import HttpResponse

def home(request):
    today = Meeting.objects.order_by('-date')[0]
    comments = Comment.objects.all()
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
    print("================================================================")
    meeting = Meeting.objects.get(id=meeting_id)
    comments = Comment.objects.all()
    return render(
        request,
        'group_meeting/list_detail.html', 
        {
            'meeting':meeting,
            'comments':comments,
        }
    )
