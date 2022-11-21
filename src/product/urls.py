from rest_framework.routers import DefaultRouter

from product.views import ProductViewSet

router = DefaultRouter()

router.register(r'products', ProductViewSet, basename='products')
urlpatterns = router.urls
