from django.contrib import admin

from places.models import Place, Coordinates, Image, Details



@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('title',)


class ImageInline(admin.TabularInline):
    model = Image


class CoordinatesInline(admin.TabularInline):
    model = Coordinates


@admin.register(Details)
class DetailsAdmin(admin.ModelAdmin):
    list_display = ('title', 'coordinates')
    inlines = [ImageInline, CoordinatesInline]


admin.site.register(Coordinates)
admin.site.register(Image)
