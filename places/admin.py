from django.contrib import admin

from places.models import Place, Image, Details



@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('title',)


class ImageInline(admin.TabularInline):
    model = Image


@admin.register(Details)
class DetailsAdmin(admin.ModelAdmin):
    list_display = ('title', 'lng', 'lat')
    inlines = [ImageInline]

admin.site.register(Image)
