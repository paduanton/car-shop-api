from django.db import models
from datetime import datetime

class CarOwner(models.Model):
 
    id = models.AutoField(
        primary_key=True
    )
    name = models.CharField(
        max_length=200,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        null=False,
        blank=False
    )
    created_at = models.DateTimeField(
        default=datetime.now,
        null=False,
        blank=False
    )

    class Meta:
        db_table = 'car_owners'

class Car(models.Model):
    class Color(models.TextChoices):
        YELLOW = 'yellow',
        BLUE = 'blue',
        GRAY = 'gray',
    class Model(models.TextChoices):
        HATCH = 'hatch',
        SEDAN = 'sedan',
        CONVERTIBLE = 'convertible',

    id = models.AutoField(
        primary_key=True
    )
    car_owner = models.ForeignKey(CarOwner, on_delete=models.CASCADE)
    model = models.CharField(
        max_length=25,
        choices=Model.choices,
    )
    price = models.FloatField(null=False, blank=False)
    color = models.CharField(
        max_length=20,
        choices=Color.choices,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        null=False,
        blank=False
    )
    created_at = models.DateTimeField(
        default=datetime.now,
        null=False,
        blank=False
    )

    class Meta:
        db_table = 'cars'
