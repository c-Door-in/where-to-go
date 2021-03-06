# Generated by Django 4.0.4 on 2022-05-10 21:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='description_short',
            field=models.TextField(max_length=500, verbose_name='Короткое описание'),
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position_number', models.IntegerField(verbose_name='Порядковый номер')),
                ('image', models.ImageField(upload_to='places/image/')),
                ('place', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='imgs', to='places.place', verbose_name='Место на картинке')),
            ],
        ),
    ]
