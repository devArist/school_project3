from django.contrib import admin
from . import models
from django.utils.html import format_html

# Register your models here.
@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ['display_image', 'title', 'description', 'licenses', 'formats', 'views']
    list_display_links = ['display_image', 'title', 'description', 'licenses', 'formats', 'views']
    filter_horizontal = ['tags']

    def display_image(self, obj):
        return format_html(
            f'<img src={obj.image.url} widht=100px height=80px'
        )
    
    display_image.short_description = 'image'


@admin.register(models.Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ['display_image', 'title', 'description', 'licenses', 'formats', 'views']
    filter_horizontal = ['tags']

    def display_image(self, obj):
        return format_html(
            f'<img src={obj.image.url} width=100px height=80px'
        )
    
    display_image.short_description = 'image'


@admin.register(models.Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(models.Licenses)
class LicensesAdmin(admin.ModelAdmin):
    list_display = ['description']