from django.db import models

# Create your models here.
class Sexo(models.Model):
    id_sexo = models.AutoField(db_column='idSexo', primary_key=True) 
    sexo    = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return str(self.sexo)
    
class Mascota(models.Model):
    id_mascota       = models.AutoField(primary_key=True)
    nombre           = models.CharField(max_length=20)
    apellido         = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField(blank=False, null=False) 
    id_sexo          = models.ForeignKey('sexo',on_delete=models.CASCADE, db_column='idSexo')  
    peso             = models.FloatField(null=True)
    raza             = models.CharField(max_length=20)

    def __str__(self):
        return str(self.nombre)+" "+str(self.apellido)   
