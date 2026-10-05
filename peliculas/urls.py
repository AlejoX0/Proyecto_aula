from django.urls import path
from . import views

urlpatterns = [
    # Películas
    path("", views.lista_peliculas, name="lista_peliculas"),
    path(
        "pelicula/<int:pk>/",
        views.detalle_pelicula,
        name="detalle_pelicula"
    ),
    path(
        "pelicula/crear/",
        views.crear_pelicula,
        name="crear_pelicula"
    ),
    path(
        "pelicula/<int:pk>/editar/",
        views.editar_pelicula,
        name="editar_pelicula"
    ),
    path(
        "pelicula/<int:pk>/eliminar/",
        views.eliminar_pelicula,
        name="eliminar_pelicula"
    ),

    # Géneros
    path(
        "generos/",
        views.lista_generos,
        name="lista_generos"
    ),
    path(
        "generos/crear/",
        views.crear_genero,
        name="crear_genero"
    ),
    path(
        "generos/<int:pk>/editar/",
        views.editar_genero,
        name="editar_genero"
    ),
    path(
        "generos/<int:pk>/eliminar/",
        views.eliminar_genero,
        name="eliminar_genero"
    ),
]
