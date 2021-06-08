from django.contrib import admin
from . import models
from django.utils.html import format_html

# Register your models here.
@admin.register(models.About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['display_image', 'description']

    def display_image(self, obj):
            return format_html(
                f'<img src={obj.image.url} width=100px height=80px>'
            )

    display_image.short_description = 'image'



@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'message']


@admin.register(models.Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ['description', 'email', 'phone', 'url']


@admin.register(models.Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ['name', 'address']


@admin.register(models.SocialNetwork)
class SocialNetworkAdmin(admin.ModelAdmin):
    list_display = ['icon', 'name', 'link']


class EmployeeSocialNetworkInline(admin.StackedInline):
    model = models.EmployeeSocialNetwork
    extra = 1

@admin.register(models.EmployeeSocialNetwork)
class EmployeeSocialNetworkAdmin(admin.ModelAdmin):
    list_display = ['icon', 'name', 'link', 'employee']

@admin.register(models.Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['display_image', 'name', 'job', 'description']
    inlines = [EmployeeSocialNetworkInline]

    def display_image(self, obj):
        return format_html(
            f'<img src={obj.image.url} width=100px height=80px>'
        )

    display_image.short_description = 'image'