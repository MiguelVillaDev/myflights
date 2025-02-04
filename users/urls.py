from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import UserView, RoleView, WDView

router = DefaultRouter()
router.register(r'user',UserView,'user')
router.register(r'role', RoleView,'role')
router.register(r'workingday', WDView,'workingday')


urlpatterns = [
    path('api/v1/', include(router.urls))
]
