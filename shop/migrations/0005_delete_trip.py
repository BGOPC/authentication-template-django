# Generated by Django 4.1.5 on 2023-02-06 15:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_alter_trip_date'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Trip',
        ),
    ]
