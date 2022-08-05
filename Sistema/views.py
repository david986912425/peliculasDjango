from multiprocessing import context
from django.shortcuts import redirect, render
from .models import Movie ,Genero,GeneroMovie

# Create your views here.
def inicio(request):
    movie = Movie.objects.all().order_by('-idmovie')[:1]
    moviePopular = Movie.objects.all()
    context = {'movie': movie,'moviePopular': moviePopular}
    return render(request, 'paginas/index.html',context)

def detalles(request,slug):
    
    if Movie.objects.filter(slug=slug).exists():
        movie = Movie.objects.get(slug=slug)
        genero = GeneroMovie.objects.filter(slug = slug)
    context = {'movie': movie,'genero':genero}   
    return render(request,'paginas/detalles.html',context)