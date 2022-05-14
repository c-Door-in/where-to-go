from django.db import models
from tinymce.models import HTMLField


class Details(models.Model):
    details_sort = models.PositiveSmallIntegerField(
        default=0,
        db_index=True,
        blank=False,
        null=False,
        verbose_name='details_sort'
    )
    title = models.CharField('Название', max_length=100)
    description_short = models.TextField(
        'Короткое описание',
        max_length=500,
        blank=True,
    )
    description_long = HTMLField('Полное описание', blank=True)
    lng = models.CharField('Долгота', max_length=50, null=True)
    lat = models.CharField('Широта', max_length=50, null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['details_sort']


class Image(models.Model):
    image = models.ImageField(upload_to='places/image/')
    place_details = models.ForeignKey(
        Details,
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
        return f'image {self.img_sort} - {self.place_details}'

    class Meta:
        ordering = ['img_sort']


class Place(models.Model):
    title = models.CharField('Название', max_length=50)
    placeId = models.CharField('Идентификатор', max_length=50, null=True)
    lng = models.CharField('Долгота', max_length=50, null=True)
    lat = models.CharField('Широта', max_length=50, null=True)
    details = models.OneToOneField(
        Details,
        on_delete=models.SET_NULL,
        related_name='place',
        verbose_name='Детальная информация',
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.title
