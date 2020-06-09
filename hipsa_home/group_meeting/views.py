from django.shortcuts import render
from .models import Meeting
import pymysql

class database:
    def __init__(self, **info):
        self.connection = pymysql.connect(user = info['user'], password = info['password'], host = info['host'])
        self.cursor = self.connection.cursor()
        self.cursor.execute('show databases')
        db = str(info['db'])
        databases = self.cursor.fetchall()

def home(request):
    params = ['165.194.123.14','hyuck2', 'hyuck2', '0625']
    connection = database(user = params[2], password = params[3], host = params[0], db=params[1])
    connection = connection.connection
    cursor = connection.cursor()
    cursor.execute("use hyuck2")

    return render(
        request,
        'group_meeting/home.html',
        {
            
        }
    )
