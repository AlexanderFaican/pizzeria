from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from .forms import FormularioLogin


def ingresar(request):
    formulario = FormularioLogin(request.POST)
    if request.method == 'POST':
        if formulario.is_valid():
         return HttpResponseRedirect(reverse('inicio'))
    else:
        return render(request, 'login/autenticar.html', {'formulario': formulario})


def cerrar(request):
    logout(request)
    return redirect(ingresar)


def inicio(request):

    return render(request, 'index.html')
