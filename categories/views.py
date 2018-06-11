from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User

from .models import Categories
from rest_framework import mixins
from rest_framework import generics

def add(request):
    if(request.method == 'POST'):
        title = request.POST['title']
        user_inst = User.objects.get(id=request.user.id)

        category = Categories(
            title=title,
            owner=user_inst
        )
        category.save()

        return redirect('/sensors')
    else:
        return render(request, 'categories/add.html')



