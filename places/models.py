from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField('Название', max_length=50)
    placeId = models.CharField('Короткое название на английском', max_length=50, null=True)
    details_title = models.CharField('Полное название места', max_length=100, blank=True)
    details_description_short = models.TextField(
        'Короткое описание',
        max_length=500,
        blank=True,
    )
    details_description_long = HTMLField('Полное описание', blank=True)
    lng = models.CharField('Долгота', max_length=50, null=True)
    lat = models.CharField('Широта', max_length=50, null=True)
    places_sort = models.PositiveSmallIntegerField(
        default=0,
        db_index=True,
        blank=False,
        null=False,
        verbose_name='Положение'
    )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['places_sort']
        verbose_name = 'Место'
        verbose_name_plural = 'Места'


class Image(models.Model):
    image = models.ImageField(
        upload_to='places/image/',
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
        blank=False,
        null=False,
        verbose_name='Порядок фоток'
    )

    def __str__(self):
        return f'{self.img_sort} - {self.place}'

    class Meta:
        ordering = ['img_sort']
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'
