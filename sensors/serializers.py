from .models import Sensors
from controllers.models import Controllers
from django.contrib.auth.models import User
from rest_framework import serializers

class SensorSerializer(serializers.ModelSerializer):
    controller = serializers.SlugRelatedField(
        read_only=True,
        slug_field='token'
    )

    class Meta:
        model = Sensors
        fields = (
            'id',
            'title',
            'description',
            'value',
            'gpio',
            'sensor_types',
            'category',
            'controller',
            'created',
            'user',
            )

class UserSerializer(serializers.ModelSerializer):
    sensors = serializers.PrimaryKeyRelatedField(many=True, queryset=Sensors.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'sensors')
