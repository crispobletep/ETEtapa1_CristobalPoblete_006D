from django import forms
from django.forms import ModelForm, widgets
from .models import Colaborador

class ColaboradorForm(ModelForm):

    class Meta:
        model = Colaborador
        fields = ['rut', 'fotografia', 'nombre', 'telefono', 'direccion', 'email', 'pais', 'password']

        labels = {
            'rut': 'RUT: ',
            'fotografia': 'Fotografia: ',
            'nombre': 'Nombre Completo: ',
            'telefono': 'Telefono: ',
            'direccion': 'Direccion: ',
            'email': 'Email: ',
            'pais': 'Pais: ',
            'password': 'Contraseña: '
        }

        widgets={

            'rut': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Digite su RUT',
                    'id': 'rut'
                }
            ),

            'fotografia': forms.TextInput(
                attrs={
                        'class': 'form-control',
                        'placeholder': 'Ingrese foto',
                        'id': 'fotografia'
                }
            ),    

            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Digite su nombre',
                    'id': 'nombre'
                }
            ),

            'telefono': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Digite su numero de telefono',
                    'id': 'telefono'
                }
            ),

            'direccion': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Digite su direccion',
                    'id': 'direccion'
                }
            ),
            
            'email': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Digite su email',
                    'id': 'email'
                }
            ),

            'pais': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Digite su pais',
                    'id': 'pais'
                }
            ),

            'password': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Digite su contraseña',
                    'id': 'password'
                }
            ),
        }