from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import GenericViewSet

from django.contrib.auth.models import User
from user.serializers import UserListSerializer


class UserViewSet(
    ListModelMixin,
    GenericViewSet,
):
    queryset = User.objects.all()
    serializer_classes = {
        'list': UserListSerializer,
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action)
