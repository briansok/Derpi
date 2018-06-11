from .models import Categories
from sensors.models import Sensors
from django.contrib.auth.models import User
from rest_framework import serializers

class CategorySerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Categories
        fields = (
            'id',
            'title',
            'users',
            'owner',
            'created',
            )

class UserSerializer(serializers.ModelSerializer):
    categories = serializers.PrimaryKeyRelatedField(many=True, queryset=Categories.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'categories')
