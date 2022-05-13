from django.contrib import admin
from django.utils.html import format_html

from places.models import Place, Image, Details



@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('title',)


class ImageInline(admin.TabularInline):
    model = Image
    fields = ('position_number', 'place_image', 'image')
    readonly_fields = ('place_image',)

    def place_image(self, obj):
        return format_html('<img src="{url}" width="{width}" height={height} />'.format(
            url = obj.image.url,
            width=obj.image.width/5,
            height=obj.image.height/5,
        )
    )


@admin.register(Details)
class DetailsAdmin(admin.ModelAdmin):
    list_display = ('title', 'lng', 'lat')
    inlines = [ImageInline]

admin.site.register(Image)
