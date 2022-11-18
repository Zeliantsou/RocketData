from django.contrib import admin

from company.models import Company


class CompanyAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'type',
        'name',
        'email',
        'country',
        'city',
        'street',
        'house_number',
        'shipper',
        'debt',
        'created',
    )


admin.site.register(Company, CompanyAdmin)
