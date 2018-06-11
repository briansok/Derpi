from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Notifications
from rest_framework import mixins
from rest_framework import generics

def index(request):
    notifications = Notifications.objects.all()[:10]

    context = {
        'notifications': notifications
    }

    if request.user.is_authenticated():
        return render(request, 'notifications/index.html', context)

    else:
        return render(request, 'notifications/homepage.html', context)

def details(request, id):
    notification = Notifications.objects.get(id=id)

    context = {
        'notification': notification

    }

    return render(request, 'notifications/details.html', context)
