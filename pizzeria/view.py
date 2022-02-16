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
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse('inicio'))
            print(user)
    else:
        formulario = FormularioLogin()
    return render(request, 'login/autenticar.html', {'formulario': formulario})


def cerrar(request):
    logout(request)
    return redirect(ingresar)


@login_required
def inicio(request):

    # lista=Persona.objects.all()#elemnto del orm objetss.all oltengo los elementos y los almaceno en lista

    # context ={
    #	'lista' : lista,
    # }
    return render(request, 'index.html')
