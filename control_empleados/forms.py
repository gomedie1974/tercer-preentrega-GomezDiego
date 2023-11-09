from django import forms


class BodegaFormulario (forms.Form):
    nombre = forms.CharField(required=True, max_length=64)
    codigo = forms.IntegerField(required=True, max_value=100000)
