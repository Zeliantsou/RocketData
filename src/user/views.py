from rest_framework.mixins import CreateModelMixin
from rest_framework.viewsets import GenericViewSet

from django.contrib.auth.models import User

from user.permissions import IsAnonymous
from user.serializers import UserCreateSerializer


class UserViewSet(
    CreateModelMixin,
    GenericViewSet,
):
    queryset = User.objects.all()
    permission_classes = (IsAnonymous,)
    serializer_classes = {
        'create': UserCreateSerializer,
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action)
