
from django.db import models

# Create your models here.
class Ciudad(models.Model):
     ciudad = models.TextField(blank=True)
     pais = models.TextField(blank=True)
     codigoPostal = models.TextField(blank=True)
     numeroAccidentes = models.TextField(blank=True)

