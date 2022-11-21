from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.mixins import (
    ListModelMixin,
    CreateModelMixin,
    DestroyModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
)
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from company.models import Company
from company.serializers import (
    CompanyListSerializer,
    CompanyCreateSerializer,
    CompanyRetrieveSerializer,
    CompanyUpdateSerializer,
)
from company.services import (
    validate_company_data,
    get_companies_with_debt_more_avg,
)


class CompanyViewSet(
    ListModelMixin,
    CreateModelMixin,
    DestroyModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    GenericViewSet,
):
    queryset = Company.objects.all()
    filter_backends = (DjangoFilterBackend, SearchFilter)
    search_fields = ('products__id',)
    filterset_fields = ('country',)
    serializer_classes = {
        'list': CompanyListSerializer,
        'create': CompanyCreateSerializer,
        'update': CompanyUpdateSerializer,
        'partial_update': CompanyUpdateSerializer,
        'retrieve': CompanyRetrieveSerializer,
        'get_with_debt_more_avg': CompanyListSerializer,
    }

    @action(methods=('get',), detail=False, url_path='with-debt-more-than-average')
    def get_with_debt_more_avg(self, request):
        companies = get_companies_with_debt_more_avg()

        page = self.paginate_queryset(companies)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(companies, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        validate_company_data(serializer.validated_data)

    def perform_update(self, serializer):
        validate_company_data(serializer.validated_data)

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action)
