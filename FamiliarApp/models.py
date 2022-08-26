from django.db import models
from datetime import datetime
# Create your models here.
class Familiar(models.Model):

    nombre=models.CharField(max_length=100)
    parentezco=models.CharField(max_length=80)
    id=models.IntegerField(primary_key=True)
    fechaCreacion= models.DateTimeField(auto_now_add=True)


