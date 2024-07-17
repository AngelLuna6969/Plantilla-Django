
#Forms de Many_Modelo
class Many_ModeloForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        #self.us = kwargs.pop('us')
        super(Many_ModeloForm, self).__init__(*args, **kwargs)
        #self.fields['sala'].queryset = Cama.objects.filter(habilitada = True,)

    class Meta:
        model = Many_Modelo
        fields = '__all__'
        exclude = ['modelo', 'usuario']
        labels = {
			'nombre_foreign':'Nombre Foreign',
			'descripcion_foreign':'Descripcion Foreign',
 
        }
        #help_texts = {}
        #error_messages = {}
        #widgets = {'field_name': forms.CheckboxSelectMultiple(), 'fecha_de_nacimiento': forms.DateInput(format=('%Y-%m-%d'),attrs={'type': 'date'})}
        pass




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
            many_modelo.usuario = request.user.perfil
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

            many_modelo.usuario = request.user.perfil
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




#URLS del modelo Many_Modelo
    path('many_modelo/crear/<str:pk>', views.many_modelo_crear_sub, name='many_modelo-crear'),
    path('many_modelo/editar/<str:pk>', views.many_modelo_editar_sub, name='many_modelo-editar'),
    path('many_modelo/eliminar/<str:pk>', views.many_modelo_eliminar_sub, name='many_modelo-eliminar'),




#Archivos del Admin Panel de Many_Modelo
class Many_ModeloAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    # a list of displayed columns name.
    list_display = ['id', 'nombre_foreign', 'descripcion_foreign']
    search_fields = ['nombre_foreign', 'descripcion_foreign']
    pass

admin.site.register(Many_Modelo, Many_ModeloAdmin)




<!-- Botón para crear el campo one to one many_modelo -->
<a href="{%url 'many_modelo-crear' dato.id%}" class="btn btn-sistema btn-dark btn-lg {%if dato.many_modelo%}disabled{%endif%}">Many_modelo</a>

<!-- Card para el campo many to one -->
{%if dato.many_modelo_set.all %}
<div class="card mt-2">
    <div class="card-header fw-bolder d-flex justify-content-between align-items-center">
        <span>{{titulo}}</span>
    </div>
    <div class="table-responsive">
        <table class="table table-striped">
            <thead>
                <tr>
                    <th style="width: 5%;" scope="col"></th>
					<th class="text-center" scope="col" style="width: auto;">Nombre_foreign</th>
					<th class="text-center" scope="col" style="width: auto;">Descripcion_foreign</th>

                    {%if request.user.is_superuser%}
                    <th style="width: 10%;" scope="col"></th>
                    {%endif%}
                </tr>
            </thead>
            <tbody class="table-group-divider">
                {%for x in dato.many_modelo_set.all %}
                <tr>
                    <th style="width: 5%;" scope="row">{{forloop.counter}}</th>
					<td style="width: auto;">{{x.nombre_foreign}}</td>
					<td style="width: auto;">{{x.descripcion_foreign}}</td>

                    {%if request.user.is_superuser and modificacion%}
                    <td style="width: 10%;">
                        <div class="btn-group" role="group">
                            <a class="btn btn-outline-dark" href="{%url 'many_modelo-editar' x.id%}"><i
                                    class="bi bi-pencil-square"></i></a>
                            <a class="btn btn-outline-dark" href="{%url 'many_modelo-eliminar' x.id%}"><i
                                    class="bi bi-trash3"></i></a>
                        </div>
                    </td>
                    {%endif%}
                </tr>
                {%endfor%}
            </tbody>
        </table>
    </div>
</div>
{%endif%}
