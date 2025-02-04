from django.db import models

# Create your models here.

sexos = (
    ('F', 'Femenino'),
    ('M', 'Masculino')
)



class Role (models.Model):
    idRole = models.AutoField(primary_key=True, unique=True)
    nameRole = models.CharField(max_length=60)
    dateRole = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['dateRole']

    def __str__ (self):
        return self.nameRole

class User (models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    rut = models.IntegerField(unique=True)
    name = models.CharField(max_length=50)
    lastName = models.CharField(max_length=80)
    age = models.IntegerField(null=False)
    sex = models.CharField(max_length=1, choices=sexos, default='M')
    email = models.EmailField(max_length=150)
    password = models.CharField(max_length=25)
    date = models.DateTimeField(auto_now=True)
    role = models.ForeignKey(Role, null=False, on_delete=models.CASCADE)
    

    class Meta:
        ordering = ['date']

    def __str__(self):
        nameComplete = self.name+ ' ' + self.lastName
        return nameComplete


class WorkingDay(models.Model):
    idWD = models.AutoField(primary_key=True, unique=True)
    start = models.DateTimeField(blank=True)
    end = models.DateTimeField(blank=True)
    worker = models.ForeignKey(User, null=False, on_delete=models.CASCADE)

    class Meta:
        ordering = ['start']

    def __int__(self):
        return self.worker



