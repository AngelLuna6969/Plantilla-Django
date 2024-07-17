
#Forms de Modelo
class ModeloForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        #self.us = kwargs.pop('us')
        super(ModeloForm, self).__init__(*args, **kwargs)
        #self.fields['sala'].queryset = Cama.objects.filter(habilitada = True,)

    class Meta:
        model = Modelo
        fields = '__all__'
        exclude = ['usuario', 'qr_code'] 
        labels = {
			'nombre':'Nombre',
			'descripcion':'Descripcion',
			'fecha':'Fecha',
			'hora':'Hora',
			'archivo':'Archivo',
			'foto':'Foto',
 
        }
        #help_texts = {}
        #error_messages = {}
        #widgets = {'field_name': forms.CheckboxSelectMultiple(), 'fecha_de_nacimiento': forms.DateInput(format=('%Y-%m-%d'),attrs={'type': 'date'})}
        pass




#Views de Modelo
@login_required(login_url='login-page')
def modelo_qr(request):
    return redirect('home')

@login_required(login_url='login-page')
def modelo_lista(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    casos = Modelo.objects.filter(
        		Q(nombre__icontains=q)|
		Q(descripcion__icontains=q)|
		Q(fecha__icontains=q)|
		Q(hora__icontains=q)|
		Q(archivo__icontains=q)|
		Q(foto__icontains=q)).order_by('id')
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
def modelo_crear(request):
    if request.method == 'POST':
        form = ModeloForm(request.POST, request.FILES, initial = {})
        if form.is_valid():
            modelo = form.save(commit=False)
			modelo.nombre = modelo.nombre.upper() if modelo.nombre else None
			modelo.descripcion = modelo.descripcion.upper() if modelo.descripcion else None
			modelo.fecha = modelo.fecha.upper() if modelo.fecha else None
			modelo.hora = modelo.hora.upper() if modelo.hora else None
			modelo.archivo = modelo.archivo.upper() if modelo.archivo else None
			modelo.foto = modelo.foto.upper() if modelo.foto else None

            modelo.usuario = request.user.perfil
            modelo.save()
            create_qrcode('modelo-qr', modelo, 'qr_code')
            messages.success(request, f'Guardado Exitosamente')
            return redirect('modelo-lista')
    else:
        form = ModeloForm()
    context = {
        'titulo': 'Crear modelo',
        'form': form,
        'btn': 'Crear',
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
			modelo.fecha = modelo.fecha.upper() if modelo.fecha else None
			modelo.hora = modelo.hora.upper() if modelo.hora else None
			modelo.archivo = modelo.archivo.upper() if modelo.archivo else None
			modelo.foto = modelo.foto.upper() if modelo.foto else None

            modelo.usuario = request.user.perfil
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
        'titulo': 'Ver modelo',
    }
    return render(request, 'modelo-ver.html', context)

#URLS del modelo Modelo
    #path('modelo/qr/<str:pk>', views.modelo_qr, name='modelo-qr'),
    path('modelo/lista', views.modelo_lista, name='modelo-lista'),
    path('modelo/ver/<str:pk>', views.modelo_ver, name='modelo-ver'),
    path('modelo/crear', views.modelo_crear, name='modelo-crear'),
    path('modelo/editar/<str:pk>', views.modelo_editar, name='modelo-editar'),
    path('modelo/eliminar/<str:pk>', views.modelo_eliminar, name='modelo-eliminar'),


#Archivos del Admin Panel de Modelo
class ModeloAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    # a list of displayed columns name.
    list_display = ['id', 'nombre', 'descripcion', 'fecha', 'hora', 'archivo', 'foto']
    search_fields = ['nombre', 'descripcion', 'fecha', 'hora', 'archivo', 'foto']
    pass

admin.site.register(Modelo, ModeloAdmin)
