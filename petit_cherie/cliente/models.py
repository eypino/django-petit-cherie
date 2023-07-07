from django.db import models
'''
GENERO_CHOICES = [
    ('M', 'Masculino'),
    ('F', 'Femenino'),
    ('O', 'Otro'),
]

class Usuario(models.Model):
    correo = models.CharField(max_length=50, blank=False, null=False)
    nombres = models.CharField(max_length=60, blank=False, null=False)
    apellidos = models.CharField(max_length=60, blank=False, null=False)
    rut = models.CharField(max_length=10, blank=False, null=False)
    fecha_nac = models.DateField(blank=False, null=False)
    telefono = models.IntegerField(blank=False, null=False)
    direccion = models.CharField(max_length=100, blank=False, null=False)
    password = models.CharField(max_length=30, blank=False, null=False)
    genero = models.CharField(max_length=1, choices=GENERO_CHOICES, blank=False, null=False, default='M')
'''