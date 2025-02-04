from rest_framework import serializers
from .models import AssignmentsTeams


class AssigmentsTeamsSerializer (serializers.ModelSerializer):
    class Meta:
        model = AssignmentsTeams
        fields = '__all__'