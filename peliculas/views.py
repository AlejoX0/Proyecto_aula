from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect, get_object_or_404

from .models import Pelicula, Genero
from .forms import PeliculaForm, GeneroForm


def es_administrador(user):
    return (
        user.is_authenticated
        and (
            user.is_staff
            or (
                hasattr(user, "perfil")
                and user.perfil.rol == "administrador"
            )
        )
    )


# =========================
# PELÍCULAS - LEER
# =========================

@login_required
def lista_peliculas(request):
    peliculas = Pelicula.objects.prefetch_related("generos")

    return render(
        request,
        "peliculas/lista.html",
        {
            "peliculas": peliculas
        }
    )


@login_required
def detalle_pelicula(request, pk):
    pelicula = get_object_or_404(
        Pelicula.objects.prefetch_related("generos"),
        pk=pk
    )

    return render(
        request,
        "peliculas/detalle.html",
        {
            "pelicula": pelicula
        }
    )


# =========================
# PELÍCULAS - CREAR
# =========================

@login_required
@user_passes_test(es_administrador)
def crear_pelicula(request):

    if request.method == "POST":
        form = PeliculaForm(request.POST)

        if form.is_valid():
            pelicula = form.save()

            messages.success(
                request,
                f'La película "{pelicula.titulo}" fue creada correctamente.'
            )

            return redirect("lista_peliculas")

    else:
        form = PeliculaForm()

    return render(
        request,
        "peliculas/formulario.html",
        {
            "form": form,
            "titulo": "Registrar película"
        }
    )


# =========================
# PELÍCULAS - ACTUALIZAR
# =========================

@login_required
@user_passes_test(es_administrador)
def editar_pelicula(request, pk):

    pelicula = get_object_or_404(Pelicula, pk=pk)

    if request.method == "POST":
        form = PeliculaForm(
            request.POST,
            instance=pelicula
        )

        if form.is_valid():
            pelicula = form.save()

            messages.success(
                request,
                f'La película "{pelicula.titulo}" fue actualizada correctamente.'
            )

            return redirect(
                "detalle_pelicula",
                pk=pelicula.pk
            )

    else:
        form = PeliculaForm(instance=pelicula)

    return render(
        request,
        "peliculas/formulario.html",
        {
            "form": form,
            "titulo": "Editar película"
        }
    )


# =========================
# PELÍCULAS - ELIMINAR
# =========================

@login_required
@user_passes_test(es_administrador)
def eliminar_pelicula(request, pk):

    pelicula = get_object_or_404(
        Pelicula,
        pk=pk
    )

    if request.method == "POST":

        titulo = pelicula.titulo

        pelicula.delete()

        messages.success(
            request,
            f'La película "{titulo}" fue eliminada correctamente.'
        )

        return redirect("lista_peliculas")

    return render(
        request,
        "peliculas/confirmar_eliminacion.html",
        {
            "objeto": pelicula,
            "tipo": "película"
        }
    )


# =========================
# GÉNEROS - LEER
# =========================

@login_required
def lista_generos(request):

    generos = Genero.objects.all()

    return render(
        request,
        "peliculas/generos.html",
        {
            "generos": generos
        }
    )


# =========================
# GÉNEROS - CREAR
# =========================

@login_required
@user_passes_test(es_administrador)
def crear_genero(request):

    if request.method == "POST":
        form = GeneroForm(request.POST)

        if form.is_valid():
            genero = form.save()

            messages.success(
                request,
                f'El género "{genero.nombre}" fue creado correctamente.'
            )

            return redirect("lista_generos")

    else:
        form = GeneroForm()

    return render(
        request,
        "peliculas/formulario.html",
        {
            "form": form,
            "titulo": "Registrar género"
        }
    )


# =========================
# GÉNEROS - ACTUALIZAR
# =========================

@login_required
@user_passes_test(es_administrador)
def editar_genero(request, pk):

    genero = get_object_or_404(
        Genero,
        pk=pk
    )

    if request.method == "POST":

        form = GeneroForm(
            request.POST,
            instance=genero
        )

        if form.is_valid():

            genero = form.save()

            messages.success(
                request,
                f'El género "{genero.nombre}" fue actualizado correctamente.'
            )

            return redirect("lista_generos")

    else:
        form = GeneroForm(instance=genero)

    return render(
        request,
        "peliculas/formulario.html",
        {
            "form": form,
            "titulo": "Editar género"
        }
    )


# =========================
# GÉNEROS - ELIMINAR
# =========================

@login_required
@user_passes_test(es_administrador)
def eliminar_genero(request, pk):

    genero = get_object_or_404(
        Genero,
        pk=pk
    )

    if request.method == "POST":

        nombre = genero.nombre

        genero.delete()

        messages.success(
            request,
            f'El género "{nombre}" fue eliminado correctamente.'
        )

        return redirect("lista_generos")

    return render(
        request,
        "peliculas/confirmar_eliminacion.html",
        {
            "objeto": genero,
            "tipo": "género"
        }
    )