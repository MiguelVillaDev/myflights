from rest_framework.routers import DefaultRouter
from django.urls import path, include

from .views import FlightView, CategoryView, BeltView, ServicesView, PCView


router = DefaultRouter()

router.register(r'flight',FlightView,'flight')
router.register(r'category',CategoryView, 'category')
router.register(r'belt',BeltView,'belt')

router.register(r'services', ServicesView, 'services')
router.register(r'payload',PCView,'payload')


urlpatterns = [
    path('api/v1/', include(router.urls))

]
