from .models import Controllers
from django.contrib.auth.models import User
from rest_framework import serializers

class ControllerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Controllers
        fields = (
            'id',
            'title',
            'token',
            'created',
            'user',
            )

class UserSerializer(serializers.ModelSerializer):
    controllers = serializers.PrimaryKeyRelatedField(many=True, queryset=Controllers.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'controllers')
