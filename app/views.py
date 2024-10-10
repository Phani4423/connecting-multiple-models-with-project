from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from app.models import *
def insert_topic(request):
    tn = input('enter insert_topic ')
    TO = topic.objects.get_or_create(topic_name = tn)
    if TO[1]:
        return HttpResponse('topic name is created')
    else:
        return HttpResponse('topic is alredy')
def insert_webpage(request):
    tn = input('topic ')
    n = input('name ')
    u = input('url ')
    e = input('email ')
    TO = topic.objects.get_or_create(topic_name=tn)[0]
    WO = topic.objects.get_or_create(topic_name= TO,name= n,url = u,email = e)
    if WO[1]:
        return HttpResponse('create')
    else:
        return HttpResponse('alredy')
