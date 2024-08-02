from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CarViewSet, CarModelViewSet, DealerViewSet

router = DefaultRouter()
router.register(r'cars', CarViewSet)
router.register(r'models', CarModelViewSet)
router.register(r'dealers', DealerViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
