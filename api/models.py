from django.db import models

# Create your models here.
class Testimonios(models.Model):
    nombre = models.CharField(max_length=50)
    pais = models.CharField(max_length=50)
    cargo = models.CharField(max_length=50)
    empresa = models.CharField(max_length=50)
    testimonio = models.CharField(max_length=50)
    