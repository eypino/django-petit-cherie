from django.db import models

# Create your models here.
class Genero(models.Model):
    id_genero = models.AutoField(db_column='idGenero', primary_key=True) 
    genero    = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return str(self.genero)
    
class TipoUsuario(models.Model):
    id_tipo_usuario = models.AutoField(db_column='idTipoUsuario', primary_key=True) 
    tipo_usuario    = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return str(self.tipo_usuario)
    


class Usuario(models.Model):
    nro_usuario         = models.AutoField(db_column='idUsuario', primary_key=True) 
    correo              = models.CharField(max_length=50, blank=False, null=False)
    p_nombre            = models.CharField(max_length=30, blank=False, null=False)
    s_nombre            = models.CharField(max_length=30)
    a_paterno           = models.CharField(max_length=30, blank=False, null=False)
    a_materno           = models.CharField(max_length=30, blank=False, null=False)
    rut                 = models.CharField(max_length=10, blank=False, null=False)
    fecha_nac           = models.DateField(blank=False, null=False)
    telefono            = models.IntegerField(blank=False, null=False)
    contraseña          = models.CharField(max_length=30, blank=False, null=False)
    id_genero           = models.ForeignKey('genero', on_delete=models.CASCADE, db_column='idGenero')
    id_tipo_usuario     = models.ForeignKey('tipo_usuario', on_delete=models.CASCADE, db_column='idTipoUsuario')

    def __str__(self):
        return str(self.p_nombre_cli+" "+self.a_paterno_cli)
    

class Producto(models.Model):
    id_producto      = models.AutoField(primary_key=True)
    nombre_producto  = models.CharField(max_length=50)
    descripcion_prod = models.CharField(max_length=20)
    valor_prod       = models.IntegerField(blank=False, null=False) 
    imagen_prod      = models.ImageField(blank=False, null=False)

    def __str__(self):
        return str(self.nombre_producto)   


class Compra(models.Model):
    nro_compra       = models.AutoField(primary_key=True)
    total            = models.IntegerField(blank=False, null=False) 
    nro_usuario      = models.ForeignKey('id_usuario', on_delete=models.CASCADE, db_column='id_usuario')

    def __str__(self):
        return str(self.nro_compra)+" "+str(self.total)

class DetalleCompra(models.Model):
    nro_item           = models.AutoField(primary_key=True)
    nro_compra         = models.ForeignKey('compra', on_delete=models.CASCADE, db_column='nro_compra', primary_key=True)
    id_producto        = models.ForeignKey('producto', on_delete=models.CASCADE, db_column='id_producto')
    cantidad           = models.IntegerField(blank=False, null=False)
    valor_item         = models.IntegerField(blank=False, null=False)

    def __str__(self):
        return str(self.id_producto)+ " " +str(self.cantidad)+ " $"+str(self.valor_item)
