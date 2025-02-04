from django.shortcuts import render
from rest_framework import viewsets

from .models import Flight, Category, Belt, Services, PayloadCompartment, Rute, Departure, Arrive, Airline, Aircraft, Gate
from . serializers import FlightSerializer, CategorySerializer, BeltSerializer, ServicesSerializer ,PCSerializer, RuteSerializer, DepartureSerializer, ArriveSerializers, AirlineSerializers, AircraftSerializers, GateSerializers

# Create your views here.


class FlightView (viewsets.ModelViewSet):
    serializer_class = FlightSerializer
    queryset = Flight.objects.all()


class CategoryView (viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class RuteView (viewsets.ModelViewSet):
    serializer_class = RuteSerializer
    queryset = Rute.objects.all()


class BeltView (viewsets.ModelViewSet):
    serializer_class = BeltSerializer 
    queryset = Belt.objects.all()


class ServicesView (viewsets.ModelViewSet):
    serializer_class = ServicesSerializer
    queryset = Services.objects.all()



class PCView (viewsets.ModelViewSet):
    serializer_class = PCSerializer
    queryset = PayloadCompartment.objects.all()


class DepartureView (viewsets.ModelViewSet):
    serializer_class = DepartureSerializer
    queryset = Departure.objects.all()

class ArriveView (viewsets.ModelViewSet):
    serializer_class = ArriveSerializers
    queryset = Arrive.objects.all()


class AirlineView (viewsets.ModelViewSet):
    serializer_class = AirlineSerializers
    queryset = Airline.objects.all()


class AircraftView (viewsets.ModelViewSet):
    serializer_class = AircraftSerializers
    queryset = Aircraft.objects.all()

class GateView (viewsets.ModelViewSet):
    serializer_class = GateSerializers
    queryset = Gate.objects.all()