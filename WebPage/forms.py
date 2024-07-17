from django import forms
from .models import Modelo, One_Modelo, Many_Modelo
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field


class ModeloForm(forms.ModelForm):
    class Meta:
        model = Modelo
        fields = '__all__'
        widgets = {
            'fecha':forms.TextInput(attrs={'type':'date'}),
            'hora':forms.TextInput(attrs={'type':'time'}),
        }


class One_ModeloForm(forms.ModelForm):
    class Meta:
        model = One_Modelo
        fields = '__all__'
        exclude = ['modelo']
        widgets = {
        } 


class Many_ModeloForm(forms.ModelForm):
    class Meta:
        model = Many_Modelo
        fields = '__all__'
        exclude = ['modelo']
        widgets = {
        } 
 
