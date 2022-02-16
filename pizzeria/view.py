from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from .forms import FormularioLogin


def ingresar(request):
    if request.method == 'POST':
        formulario = FormularioLogin(request.POST)
        if formulario.is_valid():
            usuario = request.POST['Nombre']
            clave = request.POST['Clave']
            user = authenticate(username=usuario, password=clave)
            return HttpResponseRedirect(reverse('inicio'))
    else:
        formulario = FormularioLogin()
    return render(request, 'login/autenticar.html', {'formulario': formulario})


def cerrar(request):
    logout(request)
    return redirect(ingresar)


def inicio(request):

    return render(request, 'index.html')
