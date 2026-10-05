from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.utils.http import url_has_allowed_host_and_scheme


def registro(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            return render(request, 'usuarios/registro.html', {
                'error': 'El nombre de usuario ya existe.'
            })

        usuario = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        login(request, usuario)

        return redirect('inicio')

    return render(request, 'usuarios/registro.html')


def iniciar_sesion(request):
    next_url = request.POST.get('next') or request.GET.get('next')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        usuario = authenticate(
            request,
            username=username,
            password=password
        )

        if usuario is not None:
            login(request, usuario)
            if next_url and url_has_allowed_host_and_scheme(
                next_url,
                allowed_hosts={request.get_host()},
                require_https=request.is_secure(),
            ):
                return redirect(next_url)
            return redirect('inicio')

        return render(request, 'usuarios/login.html', {
            'next': next_url,
            'error': 'Usuario o contraseña incorrectos.'
        })

    return render(request, 'usuarios/login.html', {'next': next_url})


@login_required
def cerrar_sesion(request):
    logout(request)
    return redirect('login')


@login_required
def inicio(request):
    return render(request, 'usuarios/inicio.html')
