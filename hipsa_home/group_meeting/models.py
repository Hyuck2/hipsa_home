from django.conf import settings
from django.db import models
from django.utils import timezone

class Meeting(models.Model):
    date = models.CharField(max_legth = 200)
    attendent = models.CharField(max_length = 200)
    
    def get_meetings(self):
        self.meetings = 0

    def get_topics(self):
        self.topics = 0
 