from rest_framework.mixins import (
    CreateModelMixin,
    DestroyModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
)
from rest_framework.viewsets import GenericViewSet

from product.models import Product
from product.serializers import (
    ProductCreateSerializer,
    ProductRetrieveSerializer,
    ProductUpdateSerializer,
)


class ProductViewSet(
    CreateModelMixin,
    DestroyModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    GenericViewSet,
):
    queryset = Product.objects.all()
    serializer_classes = {
        'create': ProductCreateSerializer,
        'update': ProductUpdateSerializer,
        'partial_update': ProductUpdateSerializer,
        'retrieve': ProductRetrieveSerializer,
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action)
