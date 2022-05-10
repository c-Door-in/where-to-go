from django.db import models


class Coordinate(models.Model):
    lng = models.CharField('Долгота', max_length=50)
    lat = models.CharField('Широта', max_length=50)

    def __str__(self):
        return f'{self.lng}, {self.lat}'


class Place(models.Model):
    title = models.CharField('Название', max_length=100)
    coordinates = models.OneToOneField(
        Coordinate,
        on_delete=models.SET_NULL,
        related_name='places',
        verbose_name='Координаты',
        null=True,
    )
    description_short = models.TextField('Короткое описание', max_length=300)
    description_long = models.TextField('Полное описание')

    def __str__(self):
        return self.title
