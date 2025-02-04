from rest_framework import serializers

from .models import Flight, Category, Belt, Services, PayloadCompartment


class FlightSerializer (serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = '__all__'

class CategorySerializer (serializers.ModelSerializer):
    class Meta:
        model: Category
        fields = '__all__'

""" class RuteSerializer (serializers.ModelSerializer):
    class Meta:
        model = Rute
        fields = '__all__' """


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
 