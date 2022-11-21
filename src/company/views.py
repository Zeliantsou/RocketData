from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import GenericViewSet

from company.models import Company
from company.serializers import CompanyListSerializer


class CompanyViewSet(
    ListModelMixin,
    GenericViewSet,
):
    queryset = Company.objects.all()
    serializer_classes = {
        'list': CompanyListSerializer,
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action)
