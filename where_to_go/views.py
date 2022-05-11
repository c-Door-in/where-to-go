from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render

from places.models import Place


def index_map(request):
    template = 'index_map.html'
    places_geojson = {
            'type': 'FeatureCollection',
            'features': [],
    }
    for place in Place.objects.all():
        feature = {
            'type': 'Feature',
            'geometry': {
                'type': 'Point',
                'coordinates': [place.lng, place.lat],
            },
            'properties': {
                'title': place.title,
                'placeId': place.placeId,
                'detailsUrl': f'{settings.STATIC_URL}where_to_go/places/moscow_legends.json'
            },
        }
        places_geojson['features'].append(feature)
    context = {'places_geojson': places_geojson}
    
    return render(request, template, context=context)