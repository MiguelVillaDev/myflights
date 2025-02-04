from django.shortcuts import render
from rest_framework import viewsets
from .serializers import AssigmentsTeamsSerializer
from .models import AssignmentsTeams
# Create your views here.

class AssignmentsTeamsView (viewsets.ModelViewSet):
    serializer_class = AssigmentsTeamsSerializer
    queryset = AssignmentsTeams.objects.all()