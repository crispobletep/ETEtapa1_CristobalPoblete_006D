from django.shortcuts import render, redirect
from .models import Colaborador
from .forms import ColaboradorForm

# Create your views here.

def home(request):
    nombre='Fernanda Daniela'
    colaboradores=Colaborador.objects.all()
    return render(request, 'home.html', context={'nombre_usuario':nombre, 'colab':colaboradores})

def crearColaborador(request):
    if request.method=='POST':
        colaborador_form = ColaboradorForm(request.POST)
        if colaborador_form.is_valid():
            colaborador_form.save()
            return redirect('home')
    
    else:
        colaborador_form=ColaboradorForm()
    return render(request , 'core/form_crearcolaborador.html', {'colaborador_form':colaborador_form})

def Ver(request): 
    
    colaboradores = Colaborador.objects.all()
    return render(request, 'core/ver.html', {'colaboradores':colaboradores})

def form_mod_colaborador(request, id):

    colaborador=Colaborador.objects.get(nombre=id)

    colab ={
        'form': ColaboradorForm(instance=colaborador)
    }
    if request.method == 'POST': 
        formulario = ColaboradorForm(data=request.POST, instance = colaborador)
        if formulario.is_valid: 
            formulario.save()
            return redirect('ver')
    return render(request, 'core/form_mod_colaborador.html',colab)

def form_del_colaborador(request,id):
    colaborador=Colaborador.objects.get(nombre=id)
    colaborador.delete()
    return redirect('ver')

