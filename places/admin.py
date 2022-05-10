from django.contrib import admin

from places.models import Place, Coordinate, Image


class ImageInline(admin.TabularInline):
    model = Image


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('title', 'coordinates')
    inlines = [ImageInline]


admin.site.register(Coordinate)
admin.site.register(Image)
