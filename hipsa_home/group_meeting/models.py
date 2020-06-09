from django.conf import settings
from django.db import models
from django.utils import timezone

class Meeting(models.Model):
    def get_meetings(self):
        self.meetings = 0

    def get_topics(self):
        self.topics = 0
 