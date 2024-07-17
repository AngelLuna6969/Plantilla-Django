from django.db import models

# Create your models here.

class Modelo(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
    hora = models.TimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
    archivo = models.FileField(upload_to=None, max_length=100, null=True)
    foto = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None, null=True)

    def __str__(self):
        return self.nombre
    
class One_Modelo(models.Model):
    modelo = models.OneToOneField("Modelo", on_delete=models.CASCADE, null=True, blank=False)
    nombre_complementario = models.CharField(max_length=50, null=True, blank=False)
    descripcion_complementario = models.CharField(max_length=50, null=True, blank=False)

    def __str__(self):
        return self.nombre_complementario


class Many_Modelo(models.Model):
    modelo = models.ForeignKey("Modelo", on_delete=models.CASCADE, null=True, blank=False)
    nombre_foreign = models.CharField(max_length=50, null=True, blank=False)
    descripcion_foreign = models.CharField(max_length=50, null=True, blank=False)

    def __str__(self):
        return self.nombre_foreign
