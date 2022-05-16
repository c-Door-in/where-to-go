from django.contrib import admin
from django.utils.html import format_html
from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin

from places.models import Place, Image


class SortableImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Image
    list_display = ('img_sort', 'image', 'preview')
    readonly_fields = ('preview',)
    extra = 0

    def preview(self, obj):
        return format_html('<img src="{url}" width="{width}" height={height} />'.format(
            url=obj.image.url,
            width=obj.image.width/5,
            height=obj.image.height/5,
        )
    )


@admin.register(Place)
class PlaceAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('title',)
    fieldsets = (
        (None, {
            'fields': ('title', 'placeId'),
        }),
        ('Детальная информация', {
            'fields': (
                'details_title',
                'details_description_short',
                'details_description_long',
            ),
        }),
        ('Координаты точки', {
            'fields': ('lng', 'lat'),
        }),
    )
    inlines = [SortableImageInline]

# Раскомментить, если нужны отображения группы со всеми фотографиями в админке.
# admin.site.register(Image)
