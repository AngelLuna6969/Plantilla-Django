
#Model Form f
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field
from .models import *
forms.DateInput.input_type="date"
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
        widgets = {
            'hora': forms.TimeInput(attrs={'type': 'time'}), 
            'fecha': forms.DateInput(format=('%Y-%m-%d'),attrs={'type': 'date'})}
        pass
    
class CiudadanoForm(forms.ModelForm):
    class Meta:
        model = Ciudadano
        fields = '__all__'
        exclude = ['domicilio']
        #labels = {}
        #help_texts = {}
        #error_messages = {}
        #widgets = {'qr_code': forms.ImageField(),}
    def __init__(self, *args, **kwargs):
        # self.us = kwargs.pop('us')
        super(CiudadanoForm, self).__init__(*args, **kwargs)
        # self.fields['sala'].queryset = Cama.objects.filter(habilitada = True,)
        # for field in self.fields.values():
        #     field.widget.attrs['class'] = 'form-control'
        #     field.widget.attrs['placeholder'] = 'Escribe aquí ...'
        #     field.widget.attrs['required'] = 'required'
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field('nombres'),
            Field('apellido_paterno'),
            Field('apellido_materno'),
            Field('sobrenombre'),
            Field('genero'),
            Field('telefono'),
            Field('fecha_de_nacimiento'),
            Field('observaciones'),
        )
    pass

class DomicilioForm(forms.ModelForm):
    class Meta:
        model = Domicilio
        fields = '__all__'
        # exclude = []
        
    def __init__(self, *args, **kwargs):
        super(DomicilioForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field('calle'),
            Field('numero_extorior'),
            Field('numero_interior'),
            Field('domicilio_completo')
        )
    pass

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
 
        }
        #help_texts = {}
        #error_messages = {}
        #widgets = {'field_name': forms.CheckboxSelectMultiple(), 'fecha_de_nacimiento': forms.DateInput(format=('%Y-%m-%d'),attrs={'type': 'date'})}
        pass

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