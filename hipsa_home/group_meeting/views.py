from django.shortcuts import render
import pymysql

def home(request):
    return render(
        request,
        'group_meeting/home.html',
        {
            
        }
    )

def show_users(request):
    return render(
        request,
        'group_meeting/users.html',
        {
            
        }
    )

def show_meetings(request):
    return render(
        request,
        'group_meeting/meetings.html',
        {
            
        }
    )