from django.db import models
from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission



# Create your models here.
from django.contrib.auth.models import AbstractUser

from landingpage.views import contacto



class Usuario(AbstractUser):
    email = models.EmailField(unique=True)  # Agregamos un campo para almacenar el correo electrónico
    token_verificacion = models.CharField(max_length=100, blank=True)
    activado = models.BooleanField(default=False)
    tokens_contactos = models.IntegerField(default=20)
    tokens_mensajes = models.IntegerField(default=20)
    plan = models.CharField(max_length=5, default='a')
    groups = models.ManyToManyField(Group, related_name='usuarios_grupo')
    mensajes_enviados = models.IntegerField(default=0)
    contacos_enviado = models.IntegerField(default=0)
    user_permissions = models.ManyToManyField(Permission, related_name='usuarios_permisos')
    licencia_mes = models.CharField(default=0)
    licencia_3meses = models.CharField(default=0)
    licencia_6meses = models.CharField(default=0)
    licencia_12meses = models.CharField(default=0)



    # Otros campos adicionales que desees agregar
    
    def __str__(self):
        return self.username