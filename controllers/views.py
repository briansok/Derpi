from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Controllers
import uuid

from rest_framework import mixins
from rest_framework import generics

def index(request):
    controllers = Controllers.objects.filter(user=request.user.id)

    context = {
        'controllers': controllers
    }

    if request.user.is_authenticated():
        return render(request, 'controllers/controllers.html', context)

    else:
        return render(request, 'sensors/homepage.html', context)

def details(request, id):
    controller = Controllers.objects.get(id=id)

    context = {
        'controller': controller
    }

    if request.user.is_authenticated():
        return render(request, 'controllers/details.html', context)

    else:
        return render(request, 'sensors/homepage.html', context)

def add(request):
    token = uuid.uuid4().hex

    context = {
        'token': token
    }

    if(request.method == 'POST'):
        title = request.POST['title']
        token = request.POST['token']

        user_inst = User.objects.get(id=request.user.id)

        controller = Controllers(title=title, token=token, user=user_inst)
        controller.save()


        return redirect('/controllers')

    elif request.user.is_authenticated():
        return render(request, 'controllers/add.html', context)

    else:
        return render(request, 'sensors/homepage.html', context)

def delete(request):
    if(request.method == 'POST'):
        controller_id = request.POST['controller_id']
        if controller_id:
            controller_inst = Controllers.objects.get(id=controller_id)
            controller_inst.delete()
            return redirect('/controllers')
