from django.contrib import admin

from reference.models import Country, City


class CountryAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
    )


class CityAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'country',
        'name',
    )


admin.site.register(Country, CountryAdmin)
admin.site.register(City, CityAdmin)
