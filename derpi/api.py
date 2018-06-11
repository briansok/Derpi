from categories.models import Categories
from sensors.models import Sensors
from controllers.models import Controllers
from categories.serializers import CategorySerializer
from sensors.serializers import SensorSerializer
from controllers.serializers import ControllerSerializer

from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import permissions

class CategoryList(generics.ListCreateAPIView):
    model = Categories
    serializer_class = CategorySerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        user = self.request.user
        return Categories.objects.filter(users=user)

class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Categories
    queryset = Categories.objects.all()
    serializer_class = CategorySerializer

class CategorySensors(generics.ListCreateAPIView):
    model = Sensors
    serializer_class = SensorSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        category = self.kwargs['pk']
        return Sensors.objects.filter(category=category, user=self.request.user)


class SensorList(generics.ListCreateAPIView):
    model = Sensors
    serializer_class = SensorSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        return Sensors.objects.filter(user=self.request.user)

class SensorDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Sensors
    queryset = Sensors.objects.all()
    serializer_class = SensorSerializer

class ControllerList(generics.ListCreateAPIView):
    model = Controllers
    serializer_class = ControllerSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        return Controllers.objects.filter(user=self.request.user)

class ControllerDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Controllers
    queryset = Controllers.objects.all()
    serializer_class = ControllerSerializer
