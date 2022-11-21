from rest_framework import serializers

from reference.models import Country


class CountryListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Country
        fields = (
            'id',
        )
