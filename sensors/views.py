from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User

from .models import Sensors
from controllers.models import Controllers
from categories.models import Categories
from rest_framework import mixins
from rest_framework import generics

def index(request):
    sensors = Sensors.objects.filter(user=request.user.id)[:10]
    categories = Categories.objects.filter(owner=request.user.id)

    context = {
        'sensors': sensors,
        'categories': categories
    }

    if request.user.is_authenticated():
        return render(request, 'sensors/sensors.html', context)

    else:
        return render(request, 'sensors/homepage.html', context)

def home(request):
    sensors = Sensors.objects.all()[:10]
    controllers = Controllers.objects.all()[:10]

    context = {
        'sensors': sensors,
        'controllers': controllers
    }

    if request.user.is_authenticated():
        return render(request, 'widgets/home.html', context)

    else:
        return render(request, 'sensors/homepage.html', context)

def details(request, id):
    sensor = Sensors.objects.get(id=id)

    context = {
        'sensor': sensor
    }

    if request.user.is_authenticated():
        return render(request, 'sensors/details.html', context)

    else:
        return render(request, 'sensors/homepage.html', context)

def add(request):
    controllers = Controllers.objects.filter(user=request.user.id)
    categories = Categories.objects.filter(owner=request.user.id)

    context = {
        'controllers':controllers,
        'categories':categories
    }

    if(request.method == 'POST'):
        title = request.POST['title']
        value = request.POST['value']
        gpio = request.POST['gpio']
        description = request.POST['description']
        category = request.POST['category']
        controller = request.POST['controller']
        sensor_type = request.POST['sensor_type']

        category_inst = Categories.objects.get(id=category)
        controller_inst = Controllers.objects.get(id=controller)
        user_inst = User.objects.get(id=request.user.id)

        sensor = Sensors(
            title=title,
            value=value,
            gpio=gpio,
            description=description,
            sensor_types=sensor_type,
            category=category_inst,
            controller=controller_inst,
            user=user_inst
        )
        sensor.save()

        return redirect('/sensors')

    else:
        return render(request, 'sensors/add.html', context)

def delete(request):
    if(request.method == 'POST'):
        sensor_id = request.POST['sensor_id']
        if sensor_id:
            sensor_inst = Sensors.objects.get(id=sensor_id)
            sensor_inst.delete()
            return redirect('/sensors')
