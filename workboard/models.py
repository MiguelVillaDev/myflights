from django.db import models
from assignmentsTeams.models import AssignmentsTeams

# Create your models here.

class Category (models.Model):
    idCategory = models.AutoField(primary_key=True, unique=True)
    type = models.CharField(max_length=20)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.type
    

class Rute (models.Model):
    idRute = models.AutoField(primary_key=True, unique=True)
    origin = models.CharField(max_length=10)
    destination = models.CharField(max_length=10)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        rute = self.origin + ' ' +  self.destination
        return rute
    

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

    def __str__(self):
        return super().__str__()

    
    
class Gate (models.Model):
    idGate = models.AutoField(primary_key=True, unique=True)
    numberGate = models.CharField(max_length=15)
    remote = models.BooleanField()

    def __str__(self):
        return super().__str__()
    

class Departure (models.Model):
    idDeparture = models.AutoField(primary_key=True, unique=True)
    number = models.IntegerField(blank=False)
    STD = models.TimeField()
    ATD = models.TimeField(blank=True)
    date = models.DateTimeField()
    rute = models.ManyToManyField(Rute,blank=False)
    gate = models.ForeignKey(Gate, blank=True, on_delete=models.CASCADE)
    payload = models.OneToOneField(PayloadCompartment, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return super().__str__()



class Arrive (models.Model):
    idArrive = models.AutoField(primary_key=True, unique=True)
    number = models.IntegerField(blank=False)
    STA = models.TimeField(blank=False)
    ATA = models.TimeField(blank=True)
    date = models.DateTimeField()
    rute = models.ManyToManyField(Rute,blank=False)
    gate = models.ForeignKey(Gate, blank=True, on_delete=models.CASCADE)
    belt = models.ForeignKey(Belt, blank=True, on_delete=models.CASCADE)
    payload = models.OneToOneField(PayloadCompartment, blank=True, on_delete=models.CASCADE)


    def __str__(self):
        return super().__str__()


class Aircraft (models.Model):
    idAircraft = models.AutoField(primary_key=True, unique=True)
    regristration = models.CharField(max_length=15, blank=False)
    material = models.CharField(max_length=10)
    brand = models.CharField(max_length=25)
    

    def __str__(self):
        return super().__str__()

class Airline (models.Model):
    idAirline = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=20)
    logo = models.ImageField(blank=True)
    date  =models.DateTimeField(auto_now=True)


    def __str__(self):
        return super().__str__()



class Flight (models.Model):
    idFlight = models.AutoField(primary_key=True,unique=True)
    date = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, blank=False, on_delete=models.CASCADE)
    aircraft = models.ForeignKey(Aircraft, blank=False, null=True,on_delete=models.CASCADE)
    arrive = models.OneToOneField(Arrive, blank=True, null=True, on_delete=models.CASCADE)
    departure = models.OneToOneField(Departure, blank=True, null=True, on_delete=models.CASCADE)
    service = models.ForeignKey(Services, blank=True, null=True, on_delete=models.CASCADE)
    team = models.ManyToManyField(AssignmentsTeams, blank=True)


    def __str__(self):
        return super().__str__()





