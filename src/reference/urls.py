from rest_framework.routers import DefaultRouter

from reference.views import ReferenceViewSet

router = DefaultRouter()

router.register(r'references', ReferenceViewSet, basename='references')
urlpatterns = router.urls
