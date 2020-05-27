from django.shortcuts import render


def home(request):
    return render(
        request,
        'group_meeting/home.html',
        {
            
        }
    )