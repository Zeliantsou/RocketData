from django.contrib import admin

from product.models import ProductType, Product


class ProductTypeAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
    )


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'type',
        'name',
    )


admin.site.register(ProductType, ProductTypeAdmin)
admin.site.register(Product, ProductAdmin)
