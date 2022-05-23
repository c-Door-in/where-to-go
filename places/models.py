from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField('Название', max_length=100)
    placeId = models.CharField(
        'Короткое уникальное название на английском',
        max_length=100,
        unique=True,
        null=True,
    )
    details_title = models.CharField('Полное название места', max_length=100, blank=True)
    details_description_short = models.TextField(
        'Короткое описание',
        max_length=500,
        blank=True,
    )
    details_description_long = HTMLField('Полное описание', blank=True)
    lng = models.FloatField('Долгота', max_length=50, null=True)
    lat = models.FloatField('Широта', max_length=50, null=True)
    places_sort = models.PositiveSmallIntegerField(
        default=0,
        db_index=True,
        blank=True,
        null=True,
        verbose_name='Положение'
    )

    class Meta:
        ordering = ['places_sort']
        verbose_name = 'Место'
        verbose_name_plural = 'Места'

    def __str__(self):
        return self.title


class Image(models.Model):
    image = models.ImageField(
        upload_to='places/image/',
        blank=True,
        null=True,
        verbose_name='Фотографии',
    )
    place = models.ForeignKey(
        Place,
        on_delete=models.CASCADE,
        related_name='imgs',
        verbose_name='Относится к',
        null=True,
    )

    img_sort = models.PositiveIntegerField(
        default=0,
        blank=True,
        null=True,
        verbose_name='Порядок фоток'
    )

    class Meta:
        ordering = ['img_sort']
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'

    def __str__(self):
        return f'{self.img_sort} - {self.place}'
