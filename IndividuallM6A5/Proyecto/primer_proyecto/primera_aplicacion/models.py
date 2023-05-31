from django.db import models

class Contenido(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField()
    phone = models.TextField()
    last_name = models.TextField()
    age = models.IntegerField()
    email = models.TextField()

class DatosCliente(models.Model):
    id = models.IntegerField(primary_key=True)
    direccion = models.TextField()
    edad = models.IntegerField()
    profesion = models.TextField()
    
class ContenidoProveedor(models.Model):
    id = models.IntegerField(primary_key=True)
    supplier_name = models.TextField()
    phone = models.TextField()
    email = models.TextField()
    
class DatosProveedor(models.Model):
    id = models.IntegerField(primary_key=True)
    direccion = models.TextField()
    area = models.TextField()
    producto = models.TextField()
    
    class Meta:
        permissions = (
            ("permiso_edicion", "permiso para editar card"),
        )



