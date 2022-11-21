from django.db.models import Avg
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.filters import SearchFilter
from rest_framework.mixins import (
    ListModelMixin,
    CreateModelMixin,
    DestroyModelMixin,
)
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from company.models import Company
from company.serializers import (
    CompanyListSerializer,
    CompanyCreateSerializer,
)


class CompanyViewSet(
    ListModelMixin,
    CreateModelMixin,
    DestroyModelMixin,
    GenericViewSet,
):
    queryset = Company.objects.all()
    filter_backends = (DjangoFilterBackend, SearchFilter)
    search_fields = ('products__id',)
    filterset_fields = ('country',)
    serializer_classes = {
        'list': CompanyListSerializer,
        'create': CompanyCreateSerializer,
        'get_with_debt_more_avg': CompanyListSerializer,
    }

    @action(methods=('get',), detail=False, url_path='with-debt-more-than-average')
    def get_with_debt_more_avg(self, request,):
        average_debt = Company.objects.aggregate(Avg('debt'))
        companies = Company.objects.filter(debt__gt=average_debt.get('debt__avg'))

        serializer = self.get_serializer(companies, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        data = serializer.validated_data
        company_type = data.get('type')
        shipper_type = data.get('shipper').type

        if (company_type <= shipper_type) or (company_type == 0 and shipper_type is not None):
            raise ValidationError(detail='Company type can not be less than shipper type')
        if data.get('city').country != data.get('country'):
            raise ValidationError(detail='City does not match country')

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action)
