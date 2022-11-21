from rest_framework.filters import SearchFilter
from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import GenericViewSet

from company.models import Company
from company.serializers import CompanyListSerializer


class CompanyViewSet(
    ListModelMixin,
    GenericViewSet,
):
    queryset = Company.objects.all()
    filter_backends = (SearchFilter,)
    search_fields = ('country__name',)
    serializer_classes = {
        'list': CompanyListSerializer,
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action)
