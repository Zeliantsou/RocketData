from rest_framework import serializers

from company.models import Company


class CompanyListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = (
            'id',
            'name',
            'email',
        )


class CompanyCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = (
            'type',
            'name',
            'email',
            'country',
            'city',
            'street',
            'house_number',
            'products',
            'employees',
            'shipper',
        )
