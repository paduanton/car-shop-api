from django.db import models
from datetime import datetime
import uuid

class Seller(models.Model):
     
    id = models.AutoField(
        primary_key=True
    )
    name = models.CharField(
        max_length=200,
    )
    employee_id = models.UUIDField(unique=True, blank=False, default=uuid.uuid4, editable=False)
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
        db_table = 'sellers'

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
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    model = models.CharField(
        max_length=25,
        choices=Model.choices,
    )
    price = models.FloatField(null=False, blank=False)
    color = models.CharField(
        max_length=20,
        choices=Color.choices,
    )
    available = models.BooleanField(null=False, blank=False)
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
