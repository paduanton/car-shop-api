from django.db import migrations, models
import datetime

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarOwner',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('updated_at', models.DateTimeField(auto_now_add=True, null=False, blank=False)),
                ('created_at', models.DateTimeField(default=datetime.now, null=False, blank=False)),
            ],
            options={
                'db_table': 'CarOwners',
            },
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('model', models.CharField(null=False, blank=False)),
                ('price', models.FloatField(max_length=200)),
                ('color', models.CharField(max_length=20)),
                ('updated_at', models.DateTimeField(auto_now_add=True, null=False, blank=False)),
                ('created_at', models.DateTimeField(default=datetime.now, null=False, blank=False)),
            ],
            options={
                'db_table': 'Cars',
            },
        ),
    ]
