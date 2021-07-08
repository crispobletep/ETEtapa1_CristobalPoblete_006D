from django.db import models

# Create your models here.
class Colaborador(models.Model):
    rut = models.CharField( max_length=10, primary_key=True, verbose_name='rut')
    fotografia = models.ImageField(upload_to='fotos')
    nombre = models.CharField(max_length=40, verbose_name='nombre')
    telefono = models.IntegerField(verbose_name='telefono')
    direccion = models.CharField(max_length=30, verbose_name='direccion')
    email = models.CharField(max_length=25, verbose_name='email')
    pais = models.CharField(max_length=25, verbose_name='pais')
    password = models.CharField(max_length=25, verbose_name='password')

    def __str__(self):
        return self.rut