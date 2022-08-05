from django.contrib import admin
from  .models import Movie,Genero,GeneroMovie

# Register your models here.

class GeneroMovieInline(admin.StackedInline):
    model = GeneroMovie
    extra = 0


class GeneroAdmin(admin.StackedInline):
    inlines = [GeneroMovieInline]
    list_display = ['genero']

class MovieAdmin(admin.ModelAdmin):
    inlines = [GeneroMovieInline]
    list_display = ['titulo']

admin.site.register(Genero)
admin.site.register(Movie, MovieAdmin)



