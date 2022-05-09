from django.http import HttpResponse
from django.shortcuts import render


def index_map(request):
    template = 'index_map.html'
    return render(request, template)