from django.db import models
from assignmentsTeams.models import AssignmentsTeams

# Create your models here.

class Category (models.Model):
    idCategory = models.AutoField(primary_key=True, unique=True)
    type = models.CharField(max_length=20)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.type
    

""" class Rute (models.Model):
    idRute = models.AutoField(primary_key=True, unique=True)
    origin = models.CharField(max_length=10)
    destination = models.CharField(max_length=10)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        rute = self.origin + ' ' +  self.destination
        return rute """
    

class Belt (models.Model):
    idBelt = models.AutoField(primary_key=True, unique=True)
    beltNum = models.CharField(max_length=5, null=False)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.beltNum


class Services (models.Model):
    idServices = models.AutoField(primary_key=True, unique=True)
    GPU = models.BooleanField(null=True)
    ASU = models.BooleanField(null=True)
    stair = models.BooleanField(null=True)
    parking = models.CharField(max_length=10, blank=True)
    others = models.CharField(max_length=200, blank=True)
    remarks = models.TextField(max_length=2000, blank=True)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return super().__str__()
    

class PayloadCompartment(models.Model):
    id_PC = models.AutoField(primary_key=True, unique=True)
    bag = models.IntegerField(null=True)
    cargo = models.IntegerField(null=True)
    avih = models.IntegerField(null=True)
    date = models.DateTimeField(auto_now=True)






class Flight (models.Model):
    idFlight = models.AutoField(primary_key=True,unique=True)
    airline = models.CharField(max_length=50,null=False)
    logo = models.ImageField(null=True)
    arriveNumber = models.IntegerField(null=True, blank=True)
    departureNumber = models.IntegerField(null=True, blank=True)
    registration = models.CharField(max_length=6)
    material = models.CharField(max_length=6)
    date = models.DateField(blank=False)
    gate = models.CharField(max_length=10)
    STA  = models.TimeField()
    STD = models.TimeField()
    ATA = models.TimeField()
    ATD = models.TimeField(blank=True)
    category = models.ForeignKey(Category, null=False,on_delete=models.CASCADE)
    belt = models.ForeignKey(Belt, null=True, on_delete=models.CASCADE)
    services= models.ManyToManyField(Services,blank=True)
    payload = models.ForeignKey(PayloadCompartment, null=True, blank=True, on_delete=models.CASCADE)
    team = models.ManyToManyField(AssignmentsTeams, blank=True)

    def __str__(self):
        datos = str(self.arriveNumber) + ' ' + str(self.departureNumber) + ' ' + self.registration
        return datos
    



