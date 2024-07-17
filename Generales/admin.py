
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *

# Archivos del Admin Panel de Modelo
admin.site.register(Ciudadano)
admin.site.register(Domicilio)

class ModeloAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    # a list of displayed columns name.
    list_display = ['id', 'nombre', 'descripcion',
                    'fecha', 'hora', 'archivo', 'foto']
    search_fields = ['nombre', 'descripcion',
                     'fecha', 'hora', 'archivo', 'foto']
    pass


admin.site.register(Modelo, ModeloAdmin)

# Archivos del Admin Panel de One_Modelo


class One_ModeloAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    # a list of displayed columns name.
    list_display = ['id', 'nombre_complementario',
                    'descripcion_complementario']
    search_fields = ['nombre_complementario', 'descripcion_complementario']
    pass


admin.site.register(One_Modelo, One_ModeloAdmin)

# Archivos del Admin Panel de Variante_Modelo


class Variante_ModeloAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    # a list of displayed columns name.
    list_display = ['id']
    search_fields = []
    pass


admin.site.register(Variante_Modelo, Variante_ModeloAdmin)

# Archivos del Admin Panel de Many_Modelo


class Many_ModeloAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    # a list of displayed columns name.
    list_display = ['id', 'nombre_foreign', 'descripcion_foreign']
    search_fields = ['nombre_foreign', 'descripcion_foreign']
    pass


admin.site.register(Many_Modelo, Many_ModeloAdmin)
