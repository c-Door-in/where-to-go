from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render


def index_map(request):
    template = 'index_map.html'
    context = {
        'places_geojson': {
            "type": "FeatureCollection",
            "features": [
                {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [37.62, 55.793676]
                },
                "properties": {
                    "title": "«Легенды Москвы",
                    "placeId": "moscow_legends",
                    "detailsUrl": f"{settings.STATIC_URL}where_to_go/places/moscow_legends.json"
                }
                },
                {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [37.64, 55.753676]
                },
                "properties": {
                    "title": "Крыши24.рф",
                    "placeId": "roofs24",
                    "detailsUrl": f"{settings.STATIC_URL}where_to_go/places/roofs24.json"
                }
                }
            ]
        }
    }
    return render(request, template, context=context)