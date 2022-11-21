from rest_framework.routers import DefaultRouter

from reference.views import CountryViewSet

router = DefaultRouter()

router.register(r'references', CountryViewSet, basename='references')
urlpatterns = router.urls
