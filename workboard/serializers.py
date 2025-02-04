from rest_framework import serializers

from .models import Flight, Category, Belt, Services, PayloadCompartment, Rute, Departure, Arrive, Airline, Aircraft, Gate



class FlightSerializer (serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = '__all__'

class CategorySerializer (serializers.ModelSerializer):
    class Meta:
        model: Category
        fields = '__all__'

class RuteSerializer (serializers.ModelSerializer):
    class Meta:
        model = Rute
        fields = '__all__'


class BeltSerializer (serializers.ModelSerializer):
    class Meta:
        model = Belt 
        fields = '__all__'


class ServicesSerializer (serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = '__all__'


class PCSerializer (serializers.ModelSerializer):
    class Meta:
        model = PayloadCompartment
        fields = '__all__'
 
class DepartureSerializer (serializers.ModelSerializer):
    class Meta:
        model = Departure
        fields = '__all__'


class ArriveSerializers (serializers.ModelSerializer):
    class Meta:
        model = Arrive
        fields = '__all__'



class AirlineSerializers (serializers.ModelSerializer):
    class Meta:
        model = Airline
        fields = '__all__'

class AircraftSerializers (serializers.ModelSerializer):
    class Meta:
        model = Aircraft
        fields = '__all__'

class GateSerializers (serializers.ModelSerializer):
    class Meta:
        model = Gate
        fields = '__all__'