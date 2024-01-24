# Generated by Django 3.1.3 on 2023-04-04 05:00

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('employee_id', models.CharField(max_length=500)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
            ],
            options={
                'db_table': 'sellers',
            },
        ),
        migrations.CreateModel(
            name='CarOwner',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
            ],
            options={
                'db_table': 'car_owners',
            },
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('car_owner', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='carshop.carowner')),
                ('seller', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='carshop.seller')),
                ('model', models.CharField(choices=[('hatch', 'Hatch'), ('sedan', 'Sedan'), ('convertible', 'Convertible')], max_length=25)),
                ('price', models.FloatField()),
                ('available', models.BooleanField()),
                ('color', models.CharField(choices=[('yellow', 'Yellow'), ('blue', 'Blue'), ('gray', 'Gray')], max_length=20)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
            ],
            options={
                'db_table': 'cars',
            },
        ),
    ]