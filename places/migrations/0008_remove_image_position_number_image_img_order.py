# Generated by Django 4.0.4 on 2022-05-13 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0007_details_lat_details_lng_delete_coordinates'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='position_number',
        ),
        migrations.AddField(
            model_name='image',
            name='img_order',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]