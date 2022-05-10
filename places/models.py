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
    description_short = models.TextField('Короткое описание', max_length=500)
    description_long = models.TextField('Полное описание')

    def __str__(self):
        return self.title


class Image(models.Model):
    position_number = models.IntegerField('Порядковый номер')
    image = models.ImageField(upload_to='places/image/')
    place = models.ForeignKey(
        Place,
        on_delete=models.CASCADE,
        related_name='imgs',
        verbose_name='Место на картинке',
        null=True,
        blank=True,
    )

    def __str__(self):
        return f'{self.position_number} - {self.place}'
