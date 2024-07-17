
#Forms de Variante_Modelo
class Variante_ModeloForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        #self.us = kwargs.pop('us')
        super(Variante_ModeloForm, self).__init__(*args, **kwargs)
        #self.fields['sala'].queryset = Cama.objects.filter(habilitada = True,)

    class Meta:
        model = Variante_Modelo
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




#Views de O2O Variante_Modelo
@login_required(login_url='login-page')
def variante_modelo_crear_sub(request, pk):
    v_padre = get_object_or_404(Modelo, pk=pk)
    if request.method == 'POST':
        form_variante_modelo = Variante_ModeloForm(request.POST, request.FILES, initial = {})
        if form_variante_modelo.is_valid():
            variante_modelo = form_variante_modelo.save(commit=False)
			variante_modelo.nombre_complementario = variante_modelo.nombre_complementario.upper() if variante_modelo.nombre_complementario else None
			variante_modelo.descripcion_complementario = variante_modelo.descripcion_complementario.upper() if variante_modelo.descripcion_complementario else None

            variante_modelo.usuario = request.user.perfil
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
			variante_modelo.nombre_complementario = variante_modelo.nombre_complementario.upper() if variante_modelo.nombre_complementario else None
			variante_modelo.descripcion_complementario = variante_modelo.descripcion_complementario.upper() if variante_modelo.descripcion_complementario else None

            variante_modelo.usuario = request.user.perfil
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




#URLS del modelo Variante_Modelo
    path('variante_modelo/crear/<str:pk>', views.variante_modelo_crear_sub, name='variante_modelo-crear'),
    path('variante_modelo/editar/<str:pk>', views.variante_modelo_editar_sub, name='variante_modelo-editar'),
    path('variante_modelo/eliminar/<str:pk>', views.variante_modelo_eliminar_sub, name='variante_modelo-eliminar'),




#Archivos del Admin Panel de Variante_Modelo
class Variante_ModeloAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    # a list of displayed columns name.
    list_display = ['id', 'nombre_complementario', 'descripcion_complementario']
    search_fields = ['nombre_complementario', 'descripcion_complementario']
    pass

admin.site.register(Variante_Modelo, Variante_ModeloAdmin)



"
<!-- Botón para crear el campo one to one variante_modelo -->
<a href="{%url 'variante_modelo-crear' dato.id%}" class="btn btn-sistema btn-dark btn-lg {%if dato.variante_modelo%}disabled{%endif%}">Variante_modelo</a>

<!-- Card para el campo one to one variante_modelo -->
{%if dato.variante_modelo%}
<div class="card mt-2">
    <div class="card-header fw-bolder d-flex justify-content-between align-items-center">
        <span>Variante_modelo</span>
        {%if request.user.is_superuser and modificacion%}
        <span>
            <div class="btn-group" role="group">
                <a class="btn btn-opciones btn-outline-dark" href="{%url 'variante_modelo-editar' dato.variante_modelo.id%}"><i
                        class="bi bi-pencil-square"></i></a>
                <a class="btn btn-opciones btn-outline-dark" href="{%url 'variante_modelo-eliminar' dato.variante_modelo.id%}"><i
                        class="bi bi-trash3"></i></a>
            </div>
        </span>
        {%endif%}
    </div>
    <ul class="list-group list-group-flush">

<li class="list-group-item"><span class="text-muted">Nombre_complementario:</span><span
                class="mx-2 fw-bold">{{dato.variante_modelo.nombre_complementario}}</span></li>

<li class="list-group-item"><span class="text-muted">Descripcion_complementario:</span><span
                class="mx-2 fw-bold">{{dato.variante_modelo.descripcion_complementario}}</span></li>

    </ul>
</div>
{%endif%}
