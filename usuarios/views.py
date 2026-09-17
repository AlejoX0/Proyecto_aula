from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


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
            return redirect('inicio')

        return render(request, 'usuarios/login.html', {
            'error': 'Usuario o contraseña incorrectos.'
        })

    return render(request, 'usuarios/login.html')


def cerrar_sesion(request):
    logout(request)
    return redirect('login')


def inicio(request):
    return render(request, 'usuarios/inicio.html')