import logging
import requests
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand
from pathlib import Path
from urllib.parse import unquote, urlparse

from places.models import Place, Image


logger = logging.getLogger('log')


class Command(BaseCommand):
    help = 'Parse place geoJSON format file'

    def set_logger():
        logger.setLevel(logging.DEBUG)
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        fmtstr = '%(asctime)s - %(name)s - %(levelname)s - %(funcName)s - %(message)s'
        fmtdate = '%H:%M:%S'
        formater = logging.Formatter(fmtstr, fmtdate)
        ch.setFormatter(formater)
        logger.addHandler(ch)
        return 

    def add_arguments(self, parser):
        parser.add_argument(
            nargs='+',
            type=str,
            dest='geojson_urls',
        )
        
    def handle(self, *args, **options):
        for geojson_url in options['geojson_urls']:
            self.stdout.write(self.style.WARNING(f'Загрузка данных из "{geojson_url}"'))
            response = requests.get(geojson_url)
            response.raise_for_status()
            geojson = response.json()

            title = geojson['title']
            details_description_short = geojson['description_short']
            details_description_long = geojson['description_long']
            lng = geojson['coordinates']['lng']
            lat = geojson['coordinates']['lat']

            place, created = Place.objects.get_or_create(
                placeId=title,
                defaults={
                    'title': title,
                    'details_title': title,
                    'details_description_short': details_description_short,
                    'details_description_long': details_description_long,
                    'lng': lng,
                    'lat': lat,
                },
            )
            self.stdout.write(self.style.SUCCESS(f'Загружено место "{title}"'))

            if not created:
                self.stdout.write(self.style.NOTICE(
                    f'Место "{title}" уже есть в базе. Информация будет обновлена.'
                ))
                place.title = title
                place.details_title = title
                place.details_description_short = details_description_short
                place.details_description_long = details_description_long
                place.lng = lng
                place.lat = lat
                place.save()
                place.imgs.all().delete()
                
            for image_url in geojson['imgs']:
                self.stdout.write(self.style.WARNING(
                    f'Попытка скачать картинку "{image_url}"'
                ))
                image_response = requests.get(image_url)
                response.raise_for_status()
                image_content = ContentFile(image_response.content)

                image_name = unquote(Path(urlparse(image_url).path).name)
                image = Image.objects.create(
                    place=place,
                )
                image.image.save(image_name, image_content, save=True)
                self.stdout.write(self.style.SUCCESS('Успешно!'))

        self.stdout.write(self.style.SUCCESS('Завершено выполнение скрипта!'))
    