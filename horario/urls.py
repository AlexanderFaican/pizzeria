from django.contrib import admin
from django.urls import re_path, include
from django.conf import settings
from django.conf.urls.static import static
from .import views

urlpatterns = [ 
    re_path('', views.total, name='horarios'),
    re_path('eliminar', views.eliminar),
    re_path('modificar', views.modificar),
    re_path('crear', views.crear, name='crear_horario'),
] 
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)