from urllib.parse import unquote
from django.conf import settings
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render

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


def get_place_details(request, place_id):
    place = get_object_or_404(Place, id=place_id)
    place_details = {
        'title': place.details.title,
        'imgs': [unquote(img.image.url) for img in place.details.imgs.all()],
        'description_short': place.details.description_short,
        'description_long': place.details.description_long,
        'coordinates': {
            'lng': place.details.lng,
            'lat': place.details.lat,
        },
    }
    return JsonResponse(place_details, json_dumps_params={'indent': 2,
                                                          'ensure_ascii': False})