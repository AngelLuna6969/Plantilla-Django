from django.shortcuts import render, redirect, get_object_or_404
from .forms import ModeloForm, One_ModeloForm, Many_ModeloForm
from .models import Modelo, One_Modelo, Many_Modelo
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.


def home(request):
    context = {

    }
    return render(request, 'home.html', context)


def contacto(request):
    context = {

    }
    return render(request, 'contacto.html', context)


def terminos_condiciones(request):
    context = {

    }
    return render(request, 'terminos.html', context)


def privacidad(request):
    context = {

    }
    return render(request, 'privacidad.html', context)


@csrf_exempt
def login_page(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "Este usuario no existe")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(
                request, "Bienvenido, Ingresaste Exitosamente al Sistema")
            return redirect('home')
        else:
            messages.error(request, "Usuario o contraseña no existen")
    context = {
    }
    return render(request, 'login.html', context)


@login_required(login_url="home")
def logout_page(request):
    logout(request)
    messages.success(request, "Cerraste Sesión de Manera Exitosa")
    return redirect('home')


def lista_modelos(request):
    modelos = Modelo.objects.all()
    return render(request, 'modelo_lista.html', {'datos': modelos})


def crear_modelo(request):
    if request.method == 'POST':
        form = ModeloForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_modelos')
    else:
        form = ModeloForm()
    return render(request, 'forms.html', {'form': form})


def editar_modelo(request, pk):
    modelo = get_object_or_404(Modelo, pk=pk)
    if request.method == 'POST':
        form = ModeloForm(request.POST, request.FILES, instance=modelo)
        if form.is_valid():
            form.save()
            return redirect('lista_modelos')
    else:
        form = ModeloForm(instance=modelo)
    return render(request, 'forms.html', {'form': form})


def eliminar_modelo(request, pk):
    modelo = get_object_or_404(Modelo, pk=pk)
    if request.method == 'POST':
        modelo.delete()
        return redirect('lista_modelos')
    return render(request, 'eliminar.html', {'dato': modelo})


def ver_modelo(request, pk):
    modelo = get_object_or_404(Modelo, pk=pk)
    # my_dict = {field.name: getattr(modelo, field.name) for field in modelo._meta.fields}

    return render(request, 'modelo_ver.html', {'dato': modelo, 'modificacion':True})


# Modelo one to one,
def crear_one_modelo(request, pk):
    v_padre = get_object_or_404(Modelo, pk=pk) 
    if request.method == 'POST':
        form = One_ModeloForm(request.POST, request.FILES)
        if form.is_valid():
            one_modelo = form.save(commit=False)
            one_modelo.modelo = v_padre
            one_modelo.save()
            return redirect('ver_modelo', v_padre.id)
    else:
        form = One_ModeloForm()
    return render(request, 'modelo_formulario.html', {'form': form, 'dato':v_padre})


def editar_one_modelo(request, pk):
    one_Modelo = get_object_or_404(One_Modelo, pk=pk)
    v_padre = one_Modelo.modelo
    if request.method == 'POST':
        form = One_ModeloForm(request.POST, request.FILES, instance=one_Modelo)
        if form.is_valid():
            form.save()
            return redirect('ver_modelo', v_padre.id)
    else:
        form = One_ModeloForm(instance=one_Modelo)
    return render(request, 'modelo_formulario.html', {'form': form, 'dato':v_padre})


def eliminar_one_modelo(request, pk):
    one_modelo = get_object_or_404(One_Modelo, pk=pk)
    v_padre = one_modelo.modelo
    if request.method == 'POST':
        one_modelo.delete()
        return redirect('ver_modelo', v_padre.id)
    return render(request, 'eliminar.html', {'dato': one_modelo})


# Modelo many to one
def crear_many_modelo(request, pk):
    v_padre = get_object_or_404(Modelo, pk=pk) 
    if request.method == 'POST':
        form = Many_ModeloForm(request.POST, request.FILES)
        if form.is_valid():
            one_modelo = form.save(commit=False)
            one_modelo.modelo = v_padre
            one_modelo.save()
            return redirect('ver_modelo', v_padre.id)
    else:
        form = Many_ModeloForm()
    return render(request, 'modelo_formulario.html', {'form': form, 'dato':v_padre})


def editar_many_modelo(request, pk):
    one_Modelo = get_object_or_404(Many_Modelo, pk=pk)
    v_padre = one_Modelo.modelo
    if request.method == 'POST':
        form = Many_ModeloForm(request.POST, request.FILES, instance=one_Modelo)
        if form.is_valid():
            form.save()
            return redirect('ver_modelo', v_padre.id)
    else:
        form = Many_ModeloForm(instance=one_Modelo)
    return render(request, 'modelo_formulario.html', {'form': form, 'dato':v_padre})


def eliminar_many_modelo(request, pk):
    one_modelo = get_object_or_404(Many_Modelo, pk=pk)
    v_padre = one_modelo.modelo
    if request.method == 'POST':
        one_modelo.delete()
        return redirect('ver_modelo', v_padre.id)
    return render(request, 'eliminar.html', {'dato': one_modelo})
