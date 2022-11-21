from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import GenericViewSet

from django.contrib.auth.models import User
from user.serializers import UserCreateSerializer


class UserViewSet(
    CreateModelMixin,
    GenericViewSet,
):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_classes = {
        'create': UserCreateSerializer,
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action)
