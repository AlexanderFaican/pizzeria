"""pizzeria URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  re_path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  re_path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, re_path
    2. Add a URL to urlpatterns:  re_path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import re_path, include
from django.conf import settings
from django.conf.urls.static import static
from .import view

urlpatterns = [
    re_path('admin/', admin.site.urls),
    re_path('', view.ingresar, name='login'),
    re_path('inicio/', view.inicio, name='inicio'),
    re_path('cerrarsesion/', view.cerrar, name='cerrarsesion'),
    re_path('clientes/', include('cliente.urls')),
    re_path('menus/', include('menu.urls')),
    re_path('horarios/', include('horario.urls')),
    re_path('pedidos/', include('pedido.urls'))
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_URL)
