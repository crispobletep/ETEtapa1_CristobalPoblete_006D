from django.urls import path
from . import views
from .views import home, crearColaborador, form_mod_colaborador, Ver, form_del_colaborador

urlpatterns =  [ 
    path ('' , home , name ="home"),
    path('crear_colaborador', crearColaborador, name="crear_colaborador"),
    path('ver',Ver, name="ver"),
    path('form_mod_colaborador/<id>', form_mod_colaborador, name="form_mod_colaborador"),
	path('form_del_colaborador/<id>', form_del_colaborador, name="form_del_colaborador")
]