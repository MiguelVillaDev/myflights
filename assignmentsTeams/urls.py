from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import AssignmentsTeamsView

router = DefaultRouter()

router.register(r'assignments', AssignmentsTeamsView,'assignments')

urlpatterns = [
    path('api/v1/',include(router.urls))
]