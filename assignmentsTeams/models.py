from django.db import models
from users.models import User
 
# Create your models here.


class AssignmentsTeams (models.Model):
    idTeam = models.AutoField(primary_key=True, unique=True)
    Number = models.IntegerField(null=False)
    date = models.DateTimeField()
    person = models.ManyToManyField(User)

    class Meta:
        ordering = ['date']

    def __str__ (self):
        group = "Célula " + str(self.Number)
        return group
    
  

