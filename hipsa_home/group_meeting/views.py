from django.shortcuts import render
from .models import Meeting, Topic, Comment
import pymysql

def home(request):
    meetings = Meeting.objects.all()
    today = Meeting.objects.latest('date')
    topic_ids = today.topics.split(',')
    topics = []
    comments = []
    for topic_id in topic_ids:
        t_id = int(topic_id) + 1
        selected_topic = Topic.objects.get(id = t_id)
        #topics.append(selected_topic)
        topics.append('안건 : ' + str(selected_topic.name))
        topics.append('담당 : ' + str(selected_topic.owner))
        topics.append('의견')
        p_id = int(selected_topic.id)-1
        comment = list(Comment.objects.filter(topic_id = p_id).order_by('id').values())
        space = '--'
        for c in comment:
            print(c)
            Topic.objects.get(owner = c['owner_id']-1)
            topics.append(space + str(c['description']) + ' - ' +str(int(c['owner_id'])-1))
            space = space + '--'
    print(topics)


    return render(
        request,
        'group_meeting/home.html',
        {
            'meetings':meetings,
            'today':today,
            'topics':topics,
            'comments':comments
        }
    )

def get_meeting_list(request):
    
    return render(
        request, 
        'group_meeting/meeting_list.html',
        {
        }
    )

def get_meeting(request):
    return render(
        request,
        'group_meeting/meeting.html',
        {

        }
    )

