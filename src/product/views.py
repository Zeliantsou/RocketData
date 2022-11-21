from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import GenericViewSet

from product.models import Product
from product.serializers import ProductListSerializer


class ProductViewSet(
    ListModelMixin,
    GenericViewSet,
):
    queryset = Product.objects.all()
    serializer_classes = {
        'list': ProductListSerializer,
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action)
