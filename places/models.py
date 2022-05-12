from django.db import models


class Details(models.Model):
    title = models.CharField('Название', max_length=100)
    description_short = models.TextField(
        'Короткое описание',
        max_length=500,
        blank=True,
    )
    description_long = models.TextField('Полное описание', blank=True)
    lng = models.CharField('Долгота', max_length=50, null=True)
    lat = models.CharField('Широта', max_length=50, null=True)

    def __str__(self):
        return self.title


class Image(models.Model):
    position_number = models.IntegerField('Порядковый номер')
    image = models.ImageField(upload_to='places/image/')
    place_details = models.ForeignKey(
        Details,
        on_delete=models.CASCADE,
        related_name='imgs',
        verbose_name='Относится к',
        null=True,
    )

    def __str__(self):
        return f'{self.position_number} - {self.place_details}'


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
