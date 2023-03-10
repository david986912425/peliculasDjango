from django.db import models
from autoslug import AutoSlugField
from cloudinary.models import CloudinaryField

# Create your models here.
class Genero(models.Model):
    idgenero = models.AutoField(primary_key=True)
    genero = models.CharField(verbose_name="Genero", max_length=100,null=True,blank=True)

    def __str__(self):
        fila = self.genero
        return fila

class Movie(models.Model):
    idmovie = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100,verbose_name = "Titulo")
    slug = AutoSlugField(populate_from="titulo",unique=True, null=True,verbose_name = "Slug")
    imagen = CloudinaryField(folder='Movie',verbose_name = "Imagen",null=True,blank=True)
    portada = CloudinaryField(folder='Movie',verbose_name = "Portada",null=True,blank=True)
    descripcion = models.TextField(verbose_name = "Descripcion", null=True)
    link = models.TextField(verbose_name = "Link", null=True)
    genero = models.ManyToManyField(
        Genero,
        through='GeneroMovie',
        blank=True,
    )

    def __str__(self):
        fila = self.titulo
        return fila

class GeneroMovie(models.Model):
    idgenero = models.ForeignKey(
        Genero,
        on_delete=models.CASCADE,
        blank=True, null=True
    )
    idmovie = models.ForeignKey(
        Movie, 
        on_delete=models.CASCADE,
        blank=True, null=True
    )
    slug = AutoSlugField(populate_from="idmovie",unique=False, null=True,verbose_name = "Slug")
    def __str__(self):
        return self.idmovie.titulo
