from rest_framework.mixins import (
    CreateModelMixin,
    DestroyModelMixin
)
from rest_framework.viewsets import GenericViewSet

from product.models import Product
from product.serializers import ProductCreateSerializer


class ProductViewSet(
    CreateModelMixin,
    DestroyModelMixin,
    GenericViewSet,
):
    queryset = Product.objects.all()
    serializer_classes = {
        'create': ProductCreateSerializer,
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action)
