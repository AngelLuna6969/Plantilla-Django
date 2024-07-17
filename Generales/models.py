from django.db import models

# Create your models here.

class Ciudadano(models.Model):
    GENERO = [
        ('MASCULINO', 'MASCULINO'),
        ('FEMENINO', 'FEMENINO'),
        ('OTRO', 'OTRO'),
    ]
    nombres = models.CharField(max_length=50, null=True, blank=False)
    apellido_paterno = models.CharField(max_length=50, null=True, blank=False)
    apellido_materno = models.CharField(max_length=50, null=True, blank=False)
    sobrenombre = models.CharField(max_length=50, null=True, blank=False)
    genero = models.CharField(max_length=50, null=True, blank=False, choices = GENERO)
    telefono = models.CharField(max_length=10, null=True, blank=False)
    email = models.EmailField(max_length=254, null=True, blank=False)
    fecha_de_nacimiento = models.DateField(auto_now=False, auto_now_add=False, null=True, blank = False)
    observaciones = models.TextField(null=True, blank = False)
    domicilio = models.OneToOneField("Generales.Domicilio", on_delete=models.CASCADE, null=True, blank = False)
    #foto = models.OneToOneField("Directorio.Foto", on_delete=models.CASCADE, null=True, blank=False)

    #nombre_completo = models.CharField(max_length=500, null=True, blank=False)
    #nombre_completo_sin_acentos = models.CharField(max_length=500, null=True, blank=False)
    #creo = models.ForeignKey("Usuarios.Perfil", on_delete=models.SET_NULL, null=True, blank=False, related_name = "ciudadano_creo")
    #edito = models.ForeignKey("Usuarios.Perfil", on_delete=models.SET_NULL, null=True, blank=False, related_name = "ciudadano_edito")

    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    #qr_code = models.ImageField(upload_to='ciudadanos', null=True, blank=True)
    
    def __str__(self):
        return self.nombres
    
class Domicilio(models.Model):
    calle = models.CharField(max_length=50, null=True, blank=False)
    numero_exterior = models.CharField(max_length=50, null=True, blank=False)
    numero_interior = models.CharField(max_length=50, null=True, blank=False)
    #link_maps = models.URLField(max_length=500, null=True, blank=False)
    #colonia = models.ForeignKey("Directorio.Colonia", on_delete=models.SET_NULL, null=True, blank=False)
    #codigo_postal = models.ForeignKey("Directorio.Codigo_Postal", on_delete=models.SET_NULL, null=True, blank=False)
    #municipio = models.ForeignKey("Directorio.Municipio", on_delete=models.SET_NULL, null=True, blank=False)
    #entidad = models.ForeignKey("Directorio.Entidad", on_delete=models.SET_NULL, null=True, blank=False)

    domicilio_completo = models.CharField(max_length=500, null=True, blank=False)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    #usuario = models.ForeignKey('Usuarios.Perfil', on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return self.domicilio_completo

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


class Variante_Modelo(models.Model):
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
