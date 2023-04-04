from rest_framework import serializers
from django.db import models
from .models import Car, CarOwner

class CarOwnerSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=200, required=True)

    def create(self, validated_data):
        return CarOwner.objects.create(
            name=validated_data.get('name')
        )

    class Meta:
        model = CarOwner
        fields = (
            'id',
            'name'
        )

class CarSerializer(serializers.ModelSerializer):
    class Color(models.TextChoices):
        YELLOW = 'yellow',
        BLUE = 'blue',
        GRAY = 'gray',
    model = serializers.CharField(max_length=200, required=True)
    price = serializers.FloatField(required=True)
    color = serializers.ChoiceField(
        choices=Color.choices,
        required=True
    )

    def create(self, validated_data):
        return Car.objects.create(
            car_owner=validated_data.get('car_owner'),
            model=validated_data.get('model'),
            price=validated_data.get('price'),
            color=validated_data.get('color')
        )

    class Meta:
        model = CarOwner
        fields = (
            'id',
            'car_owner',
            'model',
            'price',
            'color',
        )

