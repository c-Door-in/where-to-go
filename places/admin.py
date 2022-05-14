from django.contrib import admin
from django.utils.html import format_html
from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin

from places.models import Place, Image, Details


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('title',)


class SortableImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Image
    list_display = ('img_sort', 'image', 'place_image')
    # fields = ('img_sort','place_image', 'image')
    readonly_fields = ('place_image',)
    extra = 0

    def place_image(self, obj):
        return format_html('<img src="{url}" width="{width}" height={height} />'.format(
            url=obj.image.url,
            width=obj.image.width/5,
            height=obj.image.height/5,
        )
    )


@admin.register(Details)
class DetailsAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('title', 'lng', 'lat')
    inlines = [SortableImageInline]

admin.site.register(Image)
