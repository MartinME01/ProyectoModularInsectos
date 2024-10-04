from django.db import models

# Create your models here.

class Estado(models.Model):
    nombreEstado=models.CharField(max_length=50, verbose_name='Nombre')

    class Meta:
        verbose_name = "estado"
        verbose_name_plural = "estados"
    
    def __str__(self):
        return self.nombreEstado

class Insectos(models.Model):
    nombreInsecto = models.CharField(max_length=30, verbose_name='Nombre')
    descripcion = models.CharField(max_length=100, verbose_name='Descripcion')
    imagen = models.ImageField(upload_to='insectos')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    categoriaInsectos=models.ManyToManyField(Estado)

    class Meta:
        verbose_name = 'insecto'
        verbose_name_plural = 'insectos'
    
    def __str__(self):
        return self.nombreInsecto
