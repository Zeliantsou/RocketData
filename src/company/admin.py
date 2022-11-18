from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe

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
        'get_shipper_link',
        'debt',
        'created',
    )

    list_display_links = (
        'id',
        'name',
    )

    @admin.display(description='shipper')
    def get_shipper_link(self, obj):
        if obj.shipper:
            url = reverse(
                f"admin:{obj._meta.app_label}_{obj._meta.model_name}_change",
                args=(obj.shipper.id,)
            )
            return mark_safe(f"<a href='{url}'>{obj.shipper.name}</a>")


admin.site.register(Company, CompanyAdmin)
