from django.shortcuts import render
from rest_framework import viewsets

from .models import Flight, Category, Belt, Services, PayloadCompartment
from . serializers import FlightSerializer, CategorySerializer, BeltSerializer, ServicesSerializer ,PCSerializer

# Create your views here.


class FlightView (viewsets.ModelViewSet):
    serializer_class = FlightSerializer
    queryset = Flight.objects.all()


class CategoryView (viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


""" class RuteView (viewsets.ModelViewSet):
    serializer_class = RuteSerializer
    queryset = Rute.objects.all() """


class BeltView (viewsets.ModelViewSet):
    serializer_class = BeltSerializer 
    queryset = Belt.objects.all()


class ServicesView (viewsets.ModelViewSet):
    serializer_class = ServicesSerializer
    queryset = Services.objects.all()



class PCView (viewsets.ModelViewSet):
    serializer_class = PCSerializer
    queryset = PayloadCompartment.objects.all()