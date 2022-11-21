from django.contrib import admin, messages
from django.urls import reverse
from django.utils.safestring import mark_safe
from django.utils.translation import ngettext

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

    list_filter = ('city__name',)

    actions = ('remove_debt',)

    @admin.display(description='shipper')
    def get_shipper_link(self, obj):
        if obj.shipper:
            url = reverse(
                f"admin:{obj._meta.app_label}_{obj._meta.model_name}_change",
                args=(obj.shipper.id,)
            )
            return mark_safe(f"<a href='{url}'>{obj.shipper.name}</a>")

    @admin.action(description='Clear the debt to the supplier')
    def remove_debt(self, request, queryset):
        updated = queryset.update(debt=0)
        self.message_user(request, ngettext(
            '%d debt was successfully removed.',
            '%d debts were successfully removed.',
            updated,
        ) % updated, messages.SUCCESS)


admin.site.register(Company, CompanyAdmin)
