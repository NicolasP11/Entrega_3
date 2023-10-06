from django import forms

class comidaFormulario(forms.Form):
    nombre = forms.CharField()
    precio = forms.IntegerField()

class BuscaProdForm(forms.Form):
    nombre = forms.CharField()