from rest_framework.routers import DefaultRouter
from django.urls import path, include

from .views import FlightView, CategoryView, BeltView, ServicesView, PCView, DepartureView, ArriveView, AircraftView, AirlineView, GateView, RuteView


router = DefaultRouter()

router.register(r'flight',FlightView,'flight')
router.register(r'category',CategoryView, 'category')
router.register(r'belt',BeltView,'belt')
router.register(r'rute', RuteView, 'rute')
router.register(r'services', ServicesView, 'services')
router.register(r'payload',PCView,'payload')
router.register(r'departure',DepartureView,'departure')
router.register(r'arrive', ArriveView,'arrive')
router.register(r'aircraft', AircraftView, 'aircraft')
router.register(r'airline', AirlineView, 'airline')
router.register(r'gate', GateView, 'gate')


urlpatterns = [
    path('api/v1/', include(router.urls))

]
