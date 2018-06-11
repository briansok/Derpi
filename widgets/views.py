from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from rest_framework import mixins
from rest_framework import generics

import datetime
from .models import Widgets
from sensors.models import Sensors
from controllers.models import Controllers
from categories.models import Categories


def index(request):
    widgets = Widgets.objects.filter(user=request.user.id)
    sensors = Sensors.objects.filter(user=request.user.id)
    controllers = Controllers.objects.filter(user=request.user.id)
    now = datetime.datetime.now().strftime('%H:%M:%S')

    context = {
        'widgets': widgets,
        'sensors': sensors,
        'controllers': controllers,
        'time': now,
    }

    if request.user.is_authenticated():
        return render(request, 'widgets/home.html', context)

    else:
        return redirect('/')

def add(request):
    controllers = Controllers.objects.filter(user=request.user.id)
    sensors = Sensors.objects.filter(user=request.user.id)
    categories = Categories.objects.filter(owner=request.user.id)
    widget_clock = Widgets.objects.filter(user=request.user.id, widget_type="CL")

    context = {
        'controllers':controllers,
        'categories':categories,
        'sensors': sensors,
        'widget_clock': widget_clock,
    }

    if(request.method == 'POST'):

        user_inst = User.objects.get(id=request.user.id)
        controller_id = request.POST['controller']
        sensor_id = request.POST['sensor']
        widget = request.POST['widget']

        if widget == "clock":
            widget = Widgets(
                widget_type = "CL",
                sensors = None,
                controllers = None,
                user = user_inst
            )
            widget.save()
            return redirect('/dashboard')

        if widget == "sensor":
            sensor_inst = Sensors.objects.get(id=sensor_id)
            widget = Widgets(
                widget_type = None,
                sensors = sensor_inst,
                controllers = None,
                user = user_inst
            )
            widget.save()
            return redirect('/dashboard')

        if widget == "controller":
            controller_inst = Controllers.objects.get(id=controller_id)
            widget = Widgets(
                widget_type = None,
                sensors = None,
                controllers = controller_inst,
                user = user_inst
            )
            widget.save()
            return redirect('/dashboard')
    else:
        return render(request, 'widgets/add.html', context)

def delete(request):
    if(request.method == 'POST'):
        widget_id = request.POST['widget_id']
        if widget_id:
            widget_inst = Widgets.objects.get(id=widget_id)
            widget_inst.delete()
            return redirect('/dashboard')
