from rest_framework import viewsets
from .serializers import UserSerializer, RoleSerializer, WDSerializer
from .models import User, Role, WorkingDay

class UserView (viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()



class RoleView (viewsets.ModelViewSet):
    serializer_class = RoleSerializer
    queryset = Role.objects.all()


class WDView (viewsets.ModelViewSet):
    serializer_class = WDSerializer
    queryset = WorkingDay.objects.all()

