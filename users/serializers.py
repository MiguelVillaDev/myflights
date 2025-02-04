from rest_framework import serializers
from users.models import User, Role, WorkingDay

class UserSerializer (serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'



class RoleSerializer (serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'


class WDSerializer (serializers.ModelSerializer):
    class Meta:
        model = WorkingDay
        fields = '__all__'