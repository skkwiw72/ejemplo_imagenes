from django.db import models



# Create your models here.
class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=20, blank=True)
    intereses = models.CharField(max_length=100, blank=True)
    mensaje = models.TextField()
    acepta_privacidad = models.BooleanField()