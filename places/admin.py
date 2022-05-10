from django.contrib import admin

from places.models import Place, Coordinate


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'coordinates',
    )


admin.site.register(Coordinate)
