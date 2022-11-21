from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import GenericViewSet

from reference.models import Country
from reference.serializers import CountryListSerializer


class CountryViewSet(
    ListModelMixin,
    GenericViewSet,
):
    queryset = Country.objects.all()
    serializer_classes = {
        'list': CountryListSerializer,
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action)
