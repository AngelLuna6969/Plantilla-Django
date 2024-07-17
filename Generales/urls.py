
# Urls f
from django.urls import path
from . import views
from.views import ModeloList

urlpatterns = [
    # URLS del modelo Modelo
    # path('modelo/qr/<str:pk>', views.modelo_qr, name='modelo-qr'),
    path('modelo/lista', views.modelo_lista, name='modelo-lista'),
    path('modelo/ver/<str:pk>', views.modelo_ver, name='modelo-ver'),
    path('modelo/crear', views.modelo_crear, name='modelo-crear'),
    path('modelo/editar/<str:pk>', views.modelo_editar, name='modelo-editar'),
    path('modelo/eliminar/<str:pk>', views.modelo_eliminar, name='modelo-eliminar'),
    #URLS del modelo One_Modelo
    path('one_modelo/crear/<str:pk>', views.one_modelo_crear_sub, name='one_modelo-crear'),
    path('one_modelo/editar/<str:pk>', views.one_modelo_editar_sub, name='one_modelo-editar'),
    path('one_modelo/eliminar/<str:pk>', views.one_modelo_eliminar_sub, name='one_modelo-eliminar'),
    #URLS del modelo Variante_Modelo
    path('variante_modelo/crear/<str:pk>', views.variante_modelo_crear_sub, name='variante_modelo-crear'),
    path('variante_modelo/editar/<str:pk>', views.variante_modelo_editar_sub, name='variante_modelo-editar'),
    path('variante_modelo/eliminar/<str:pk>', views.variante_modelo_eliminar_sub, name='variante_modelo-eliminar'),
    #URLS del modelo Many_Modelo
    path('many_modelo/crear/<str:pk>', views.many_modelo_crear_sub, name='many_modelo-crear'),
    path('many_modelo/editar/<str:pk>', views.many_modelo_editar_sub, name='many_modelo-editar'),
    path('many_modelo/eliminar/<str:pk>', views.many_modelo_eliminar_sub, name='many_modelo-eliminar'),

    path('modelo/lista_modelos/', views.list_Modelos, name='modelos-prueba'),
    path('modelo/agrega/', views.agregar_Modelos, name='agrega'),
    path('api/', ModeloList.as_view(), name='modelo_list'),



]
