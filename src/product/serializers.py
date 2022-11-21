from rest_framework import serializers

from product.models import Product


class ProductCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = (
            'name',
            'type',
            'release_date',
        )
