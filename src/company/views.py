from django.db.models import Avg
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.mixins import ListModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from company.models import Company
from company.serializers import CompanyListSerializer


class CompanyViewSet(
    ListModelMixin,
    GenericViewSet,
):
    queryset = Company.objects.all()
    filter_backends = (DjangoFilterBackend, SearchFilter)
    search_fields = ('products__id',)
    filterset_fields = ('country',)
    serializer_classes = {
        'list': CompanyListSerializer,
        'get_with_debt_more_avg': CompanyListSerializer,
    }

    @action(methods=('get',), detail=False, url_path='with-debt-more-than-average')
    def get_with_debt_more_avg(self, request,):
        average_debt = Company.objects.aggregate(Avg('debt'))
        companies = Company.objects.filter(debt__gt=average_debt.get('debt__avg'))

        serializer = self.get_serializer(companies, many=True)
        return Response(serializer.data)

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action)
