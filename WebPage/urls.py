from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path("contacto/", views.contacto, name='contacto'),
    path("terminos-y-condiciones/", views.terminos_condiciones, name='terminos'),
    path("politica-de-privacidad/", views.privacidad, name='privacidad'),
    path("login/", views.login_page, name='login-page'),
    path("logout/", views.logout_page, name='logout-page'),

    path('lista/', views.lista_modelos, name='lista_modelosx'),
    path('crear/', views.crear_modelo, name='modelox-crear'),
    path('editar/<int:pk>/', views.editar_modelo, name='editar_modelox'),
    path('ver/<int:pk>/', views.ver_modelo, name='ver_modelox'),
    path('eliminar/<int:pk>/', views.eliminar_modelo, name='eliminar_modelox'),
    #Variables one to one
    path('one-modelo/crear/<int:pk>', views.crear_one_modelo, name='one_modelox-crear'),
    path('one-modelo/editar/<int:pk>', views.editar_one_modelo, name='editar_one_modelox'),
    path('one-modelo/eliminar/<int:pk>', views.eliminar_one_modelo, name='eliminar_one_modelox'),
    #Variables one to one
    path('many-modelo/crear/<int:pk>', views.crear_many_modelo, name='many_modelox-crear'),
    path('many-modelo/editar/<int:pk>', views.editar_many_modelo, name='editar_many_modelox'),
    path('many-modelo/eliminar/<int:pk>', views.eliminar_many_modelo, name='eliminar_many_modelox'),
    
]
