# Generated by Django 4.1.5 on 2023-02-12 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carpool', '0005_remove_ride_departure_time_ride_departure_day_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ride',
            name='destination',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='ride',
            name='origin',
            field=models.CharField(max_length=100),
        ),
    ]
