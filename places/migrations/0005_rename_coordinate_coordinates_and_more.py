# Generated by Django 4.0.4 on 2022-05-11 16:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0004_alter_place_properties'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Coordinate',
            new_name='Coordinates',
        ),
        migrations.RenameModel(
            old_name='detailsUrl',
            new_name='Details',
        ),
    ]
