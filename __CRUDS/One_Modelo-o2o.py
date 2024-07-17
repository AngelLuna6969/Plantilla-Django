
#Forms de One_Modelo
class One_ModeloForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        #self.us = kwargs.pop('us')
        super(One_ModeloForm, self).__init__(*args, **kwargs)
        #self.fields['sala'].queryset = Cama.objects.filter(habilitada = True,)

    class Meta:
        model = One_Modelo
        fields = '__all__'
        exclude = ['modelo', 'usuario']
        labels = {
			'nombre_complementario':'Nombre Complementario',
			'descripcion_complementario':'Descripcion Complementario',
 
        }
        #help_texts = {}
        #error_messages = {}
        #widgets = {'field_name': forms.CheckboxSelectMultiple(), 'fecha_de_nacimiento': forms.DateInput(format=('%Y-%m-%d'),attrs={'type': 'date'})}
        pass




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

            one_modelo.usuario = request.user.perfil
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
    return render(request, 'Generales/modelo-formulario.html', context)


@login_required(login_url='login-page')
def one_modelo_editar_sub(request, pk):
    one_modelo = get_object_or_404(One_Modelo, pk=pk)
    if request.method == 'POST':
        form = One_ModeloForm(request.POST, request.FILES, instance=one_modelo)
        if form.is_valid():
            one_modelo = form.save(commit=False)
			one_modelo.nombre_complementario = one_modelo.nombre_complementario.upper() if one_modelo.nombre_complementario else None
			one_modelo.descripcion_complementario = one_modelo.descripcion_complementario.upper() if one_modelo.descripcion_complementario else None

            one_modelo.usuario = request.user.perfil
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
    return render(request, 'Generales/modelo-formulario.html', context)

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
    return render(request, 'Main/validacion_delete.html', context)




#URLS del modelo One_Modelo
    path('one_modelo/crear/<str:pk>', views.one_modelo_crear_sub, name='one_modelo-crear'),
    path('one_modelo/editar/<str:pk>', views.one_modelo_editar_sub, name='one_modelo-editar'),
    path('one_modelo/eliminar/<str:pk>', views.one_modelo_eliminar_sub, name='one_modelo-eliminar'),




#Archivos del Admin Panel de One_Modelo
class One_ModeloAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    # a list of displayed columns name.
    list_display = ['id', 'nombre_complementario', 'descripcion_complementario']
    search_fields = ['nombre_complementario', 'descripcion_complementario']
    pass

admin.site.register(One_Modelo, One_ModeloAdmin)



"
<!-- Botón para crear el campo one to one one_modelo -->
<a href="{%url 'one_modelo-crear' dato.id%}" class="btn btn-sistema btn-dark btn-lg {%if dato.one_modelo%}disabled{%endif%}">One_modelo</a>

<!-- Card para el campo one to one one_modelo -->
{%if dato.one_modelo%}
<div class="card mt-2">
    <div class="card-header fw-bolder d-flex justify-content-between align-items-center">
        <span>One_modelo</span>
        {%if request.user.is_superuser and modificacion%}
        <span>
            <div class="btn-group" role="group">
                <a class="btn btn-opciones btn-outline-dark" href="{%url 'editar-one_modelo' dato.one_modelo.id%}"><i
                        class="bi bi-pencil-square"></i></a>
                <a class="btn btn-opciones btn-outline-dark" href="{%url 'eliminar-one_modelo' dato.one_modelo.id%}"><i
                        class="bi bi-trash3"></i></a>
            </div>
        </span>
        {%endif%}
    </div>
    <ul class="list-group list-group-flush">

<li class="list-group-item"><span class="text-muted">Nombre_complementario:</span><span
                class="mx-2 fw-bold">{{dato.nombre_complementario}}</span></li>

<li class="list-group-item"><span class="text-muted">Descripcion_complementario:</span><span
                class="mx-2 fw-bold">{{dato.descripcion_complementario}}</span></li>

    </ul>
</div>
{%endif%}
