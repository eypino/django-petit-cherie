from django.db import models

# Create your models here.
class Genero(models.Model):
    id_genero = models.AutoField(db_column='idGenero', primary_key=True) 
    genero    = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return str(self.genero)
    

class Cliente(models.Model):
    nro_cliente         = models.AutoField(db_column='idCliente', primary_key=True) 
    correo_cliente      = models.CharField(max_length=50, blank=False, null=False)
    p_nombre_cli        = models.CharField(max_length=30, blank=False, null=False)
    s_nombre_cli        = models.CharField(max_length=30)
    a_paterno_cli       = models.CharField(max_length=30, blank=False, null=False)
    a_materno_cli       = models.CharField(max_length=30, blank=False, null=False)
    rut_cli             = models.CharField(max_length=10, blank=False, null=False)
    fecha_nac_cli       = models.DateField(blank=False, null=False)
    telefono_cli        = models.IntegerField(blank=False, null=False)
    contraseña_cli      = models.CharField(max_length=30, blank=False, null=False)
    id_genero           = models.ForeignKey('genero', on_delete=models.CASCADE, db_column='idGenero')

    def __str__(self):
        return str(self.p_nombre_cli+" "+self.a_paterno_cli)
    

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
