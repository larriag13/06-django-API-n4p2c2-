from django import forms
from django.core import validators
from .models import Empleado

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ['nombre', 'email', 'telefono']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
        }
        validators = {
            'email': [validators.validate_email],
        }
    nombre=forms.CharField(
        required=True,
        min_length=3,
        max_length=100,
        # validators=[
        #     validators.MinLengthValidator(3),
        #     validators.MaxLengthValidator(100),
        # ]
        )

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if not nombre.isalpha():
            raise forms.ValidationError("El nombre solo puede contener letras.")
        return nombre