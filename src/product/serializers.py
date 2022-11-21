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


class ProductRetrieveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'type',
            'release_date',
        )


class ProductUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = (
            'name',
            'type',
            'release_date',
        )
