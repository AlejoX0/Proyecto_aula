from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Genero(models.Model):
    nombre = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="Nombre"
    )

    descripcion = models.TextField(
        blank=True,
        verbose_name="Descripción"
    )

    class Meta:
        ordering = ["nombre"]
        verbose_name = "Género"
        verbose_name_plural = "Géneros"

    def __str__(self):
        return self.nombre


class Pelicula(models.Model):
    titulo = models.CharField(
        max_length=200,
        verbose_name="Título"
    )

    sinopsis = models.TextField(
        verbose_name="Sinopsis"
    )

    anio = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1888),
            MaxValueValidator(2100)
        ],
        verbose_name="Año"
    )

    duracion = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1)
        ],
        verbose_name="Duración en minutos"
    )

    imagen = models.URLField(
        blank=True,
        verbose_name="URL del póster"
    )

    generos = models.ManyToManyField(
        Genero,
        related_name="peliculas",
        verbose_name="Géneros"
    )

    fecha_creacion = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ["titulo"]
        verbose_name = "Película"
        verbose_name_plural = "Películas"

    def __str__(self):
        return self.titulo