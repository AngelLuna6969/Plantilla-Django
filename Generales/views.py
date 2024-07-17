
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from datetime import date
from django.forms import modelformset_factory
from django.db.models import Q, Sum
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from rest_framework import generics
from .serializers import ModeloSerializer
from django.core.files import File
img = File(open('_static\images\logo.png', 'rb'))

# Views de Modelo


@login_required(login_url='login-page')
def modelo_qr(request):
    return redirect('home')


@login_required(login_url='login-page')
def modelo_lista(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    casos = Modelo.objects.filter(
        Q(nombre__icontains=q) |
        Q(descripcion__icontains=q)).order_by('id')
    paginator = Paginator(casos, 50)
    page_number = request.GET.get('page')
    datos = paginator.get_page(page_number)
    context = {
        'datos': datos,
        'titulo': 'Lista de modelos',
        'nombre_boton': 'Crear modelo',
    }
    return render(request, 'modelo-lista.html', context)

@login_required(login_url='login-page')
def list_Modelos(request):
    modelos=list(Modelo.objects.values())
    data={'modelos':modelos}
    return JsonResponse(data)

@login_required(login_url='login-page')
def agregar_Modelos(request):
    for i in range(8000):
        modelo = Modelo()
        modelo.nombre = 'ANGEL'
        modelo.descripcion = 'DESCRIPCION'
        modelo.fecha = date.today()
        modelo.hora = '08:10:00'
        modelo.archivo=img
        modelo.foto=img
        modelo.save()
    return redirect('modelo-lista')

class ModeloList(generics.ListCreateAPIView):
    queryset = Modelo.objects.all()
    serializer_class = ModeloSerializer


# @login_required(login_url='login-page')
# def modelo_crear(request):
#     if request.method == 'POST':
#         form = ModeloForm(request.POST, request.FILES, initial={})
#         if form.is_valid():
#             modelo = form.save(commit=False)
#             modelo.nombre = modelo.nombre.upper() if modelo.nombre else None
#             modelo.descripcion = modelo.descripcion.upper() if modelo.descripcion else None
#             modelo.save()
#             messages.success(request, f'Guardado Exitosamente')
#             return redirect('modelo-lista')
#     else:
#         form = ModeloForm(),
#         domicilio_form=DomicilioForm()
#     context = {
#         'titulo': 'Crear Usuario',
#         'form': form,
#         'domicilio_form':domicilio_form,
#         'btn': 'Crear',
#     }
#     return render(request, 'forms.html', context)

# @login_required(login_url='login-page')
# def modelo_crear(request):
#     if request.method == 'POST':
#         form = CiudadanoForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, f'Guardado Exitosamente')
#             return redirect('modelo-lista')
#     else:
#         form = CiudadanoForm()
#         domicilio_form=DomicilioForm()
#     context = {
#         'titulo': 'Crear Usuario',
#         'form': form,
#         'titulo_form':'Datos del Ciudadano',
#         'form_d':domicilio_form,
#         'titulo_form_d':'Datos del Domicilio',
#     }
#     return render(request, 'forms.html', context)

@login_required(login_url='login-page')
def modelo_crear(request):
    if request.method == 'POST':
        form = CiudadanoForm(request.POST, request.FILES, instance=None)
        domicilio_form=DomicilioForm(request.POST, request.FILES, instance=None)
        if form.is_valid() and domicilio_form.is_valid():
            domicilio=domicilio_form.save(commit=False)
            domicilio.save()
            ciudadano = form.save(commit=False)
            ciudadano.domicilio = domicilio
            ciudadano.save()
            messages.success(request, f'Guardado Exitosamente')
            return redirect('modelo-lista')
    else:
        form = CiudadanoForm()
        domicilio_form=DomicilioForm()
    context = {
        'titulo': 'Crear Usuario',
        'form': form,
        'titulo_form':'Datos del Ciudadano',
        'form_d':domicilio_form,
        'titulo_form_d':'Datos del Domicilio',
    }
    return render(request, 'forms.html', context)


@login_required(login_url='login-page')
def modelo_editar(request, pk):
    modelo = get_object_or_404(Modelo, pk=pk)
    if request.method == 'POST':
        form = ModeloForm(request.POST, request.FILES, instance=modelo)
        if form.is_valid():
            modelo = form.save(commit=False)
            modelo.nombre = modelo.nombre.upper() if modelo.nombre else None
            modelo.descripcion = modelo.descripcion.upper() if modelo.descripcion else None
            modelo.save()
            messages.success(request, f'Guardado Exitosamente')
            return redirect('modelo-ver', modelo.id)
    else:
        form = ModeloForm(instance=modelo)
    context = {
        'titulo': 'Editar modelo',
        'form': form,
        'btn': 'Editar',
    }
    return render(request, 'forms.html', context)


@login_required(login_url='login-page')
def modelo_eliminar(request, pk):
    modelo = get_object_or_404(Modelo, pk=pk)
    if request.method == 'POST':
        modelo.delete()
        return redirect('modelo-lista')
    context = {
        'dato': modelo,
        'titulo': 'Eliminar modelo',
        'btn': 'Eliminar',
    }
    return render(request, 'eliminar.html', context)


@login_required(login_url='login-page')
def modelo_ver(request, pk):
    modelo = get_object_or_404(Modelo, pk=pk)
    context = {
        'dato': modelo,
        'modificacion': True,
        'titulo': 'Ver modelo',
    }
    return render(request, 'modelo-ver.html', context)

#Views de O2O One_Modelo
@login_required(login_url='login-page')
def one_modelo_crear_sub(request, pk):
    v_padre = get_object_or_404(Modelo, pk=pk)
    if request.method == 'POST':
        form_one_modelo = One_ModeloForm(request.POST, request.FILES, initial = {})
        if form_one_modelo.is_valid():
            one_modelo = form_one_modelo.save(commit=False)
            one_modelo.nombre_complementario = one_modelo.nombre_complementario.upper() if one_modelo.nombre_complementario else None
            one_modelo.descripcion_complementario = one_modelo.descripcion_complementario.upper() if one_modelo.descripcion_complementario else None
            #one_modelo.usuario = request.user.perfil
            one_modelo.modelo = v_padre
            one_modelo.save()
            #create_qrcode('one_modelo-qr', one_modelo, 'qr_code')
            messages.success(request, f'Guardado Exitosamente')
            return redirect('modelo-ver', v_padre.id)
    else:
        form_one_modelo = One_ModeloForm()
    context = {
        'dato' : v_padre,
        'titulo': 'Crear one modelo',
        'form': form_one_modelo,
        'btn': 'Crear',
    }
    return render(request, 'modelo-formulario.html', context)


@login_required(login_url='login-page')
def one_modelo_editar_sub(request, pk):
    one_modelo = get_object_or_404(One_Modelo, pk=pk)
    if request.method == 'POST':
        form = One_ModeloForm(request.POST, request.FILES, instance=one_modelo)
        if form.is_valid():
            one_modelo = form.save(commit=False)
            one_modelo.nombre_complementario = one_modelo.nombre_complementario.upper() if one_modelo.nombre_complementario else None
            one_modelo.descripcion_complementario = one_modelo.descripcion_complementario.upper() if one_modelo.descripcion_complementario else None
            #one_modelo.usuario = request.user.perfil
            one_modelo.save()
            messages.success(request, f'Guardado Exitosamente')
            return redirect('modelo-ver', one_modelo.modelo.id)
    else:
        form = One_ModeloForm(instance=one_modelo)
    context = {
        'titulo': 'Editar one modelo',
        'dato': one_modelo.modelo,
        'form': form,
        'btn': 'Editar',
    }
    return render(request, 'modelo-formulario.html', context)

@login_required(login_url='login-page')
def one_modelo_eliminar_sub(request, pk):
    one_modelo = get_object_or_404(One_Modelo, pk=pk)
    var = one_modelo.modelo
    if request.method == 'POST':
        one_modelo.delete()
        return redirect('modelo-ver', var.id)
    context = {
        'dato': one_modelo,
        'titulo': 'Eliminar one modelo',
        'btn': 'Eliminar',
    }
    return render(request, 'eliminar.html', context)

#Views de O2O Variante_Modelo
@login_required(login_url='login-page')
def variante_modelo_crear_sub(request, pk):
    v_padre = get_object_or_404(Modelo, pk=pk)
    if request.method == 'POST':
        form_variante_modelo = Variante_ModeloForm(request.POST, request.FILES, initial = {})
        if form_variante_modelo.is_valid():
            variante_modelo = form_variante_modelo.save(commit=False)

            #variante_modelo.usuario = request.user.perfil
            variante_modelo.modelo = v_padre
            variante_modelo.save()
            #create_qrcode('variante_modelo-qr', variante_modelo, 'qr_code')
            messages.success(request, f'Guardado Exitosamente')
            return redirect('modelo-ver', v_padre.id)
    else:
        form_variante_modelo = Variante_ModeloForm()
    context = {
        'dato' : v_padre,
        'titulo': 'Crear variante modelo',
        'form': form_variante_modelo,
        'btn': 'Crear',
    }
    return render(request, 'modelo-formulario.html', context)


@login_required(login_url='login-page')
def variante_modelo_editar_sub(request, pk):
    variante_modelo = get_object_or_404(Variante_Modelo, pk=pk)
    if request.method == 'POST':
        form = Variante_ModeloForm(request.POST, request.FILES, instance=variante_modelo)
        if form.is_valid():
            variante_modelo = form.save(commit=False)

            #variante_modelo.usuario = request.user.perfil
            variante_modelo.save()
            messages.success(request, f'Guardado Exitosamente')
            return redirect('modelo-ver', variante_modelo.modelo.id)
    else:
        form = Variante_ModeloForm(instance=variante_modelo)
    context = {
        'titulo': 'Editar variante modelo',
        'dato': variante_modelo.modelo,
        'form': form,
        'btn': 'Editar',
    }
    return render(request, 'modelo-formulario.html', context)

@login_required(login_url='login-page')
def variante_modelo_eliminar_sub(request, pk):
    variante_modelo = get_object_or_404(Variante_Modelo, pk=pk)
    var = variante_modelo.modelo
    if request.method == 'POST':
        variante_modelo.delete()
        return redirect('modelo-ver', var.id)
    context = {
        'dato': variante_modelo,
        'titulo': 'Eliminar variante modelo',
        'btn': 'Eliminar',
    }
    return render(request, 'eliminar.html', context)

#Views de M2O Many_Modelo
@login_required(login_url='login-page')
def many_modelo_crear_sub(request, pk):
    v_padre = get_object_or_404(Modelo, pk=pk)
    if request.method == 'POST':
        form_many_modelo = Many_ModeloForm(request.POST, request.FILES, initial = {})
        if form_many_modelo.is_valid():
            many_modelo = form_many_modelo.save(commit=False)
            many_modelo.nombre_foreign = many_modelo.nombre_foreign.upper() if many_modelo.nombre_foreign else None
            many_modelo.descripcion_foreign = many_modelo.descripcion_foreign.upper() if many_modelo.descripcion_foreign else None

            many_modelo.modelo = v_padre
            #many_modelo.usuario = request.user.perfil
            many_modelo.save()
            v_padre.modelo = many_modelo
            v_padre.save()
            messages.success(request, f'Guardado Exitosamente')
            return redirect('modelo-ver', v_padre.id)
    else:
        form_many_modelo = Many_ModeloForm()
    context = {
        'dato' : v_padre,
        'titulo': 'Crear many modelo',
        'form': form_many_modelo,
        'btn': 'Crear',
    }
    return render(request, 'modelo-formulario.html', context)


@login_required(login_url='login-page')
def many_modelo_editar_sub(request, pk):
    many_modelo = get_object_or_404(Many_Modelo, pk=pk)
    if request.method == 'POST':
        form = Many_ModeloForm(request.POST, request.FILES, instance=many_modelo)
        if form.is_valid():
            many_modelo = form.save(commit=False)
            many_modelo.nombre_foreign = many_modelo.nombre_foreign.upper() if many_modelo.nombre_foreign else None
            many_modelo.descripcion_foreign = many_modelo.descripcion_foreign.upper() if many_modelo.descripcion_foreign else None

            #many_modelo.usuario = request.user.perfil
            many_modelo.save()
            messages.success(request, f'Guardado Exitosamente')
            return redirect('modelo-ver', many_modelo.modelo.id)
    else:
        form = Many_ModeloForm(instance=many_modelo)
    context = {
        'titulo': 'Editar many modelo',
        'dato': many_modelo.modelo,
        'form': form,
        'btn': 'Editar',
    }
    return render(request, 'modelo-formulario.html', context)

@login_required(login_url='login-page')
def many_modelo_eliminar_sub(request, pk):
    many_modelo = get_object_or_404(Many_Modelo, pk=pk)
    var = many_modelo.modelo
    if request.method == 'POST':
        many_modelo.delete()
        return redirect('modelo-ver', var.id)
    context = {
        'dato': many_modelo,
        'titulo': 'Eliminar many modelo',
        'btn': 'Eliminar',
    }
    return render(request, 'eliminar.html', context)
