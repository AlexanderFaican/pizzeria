from django.shortcuts import render
from rest_framework import viewsets
##SE AGREGO 1
#from django_filters.rest_framework import DjangoFilterBackend
#from rest_framework import filters

##from api.core.legal.serializers import *
##from app.core.legal.models import *
from api.serializers import HorarioSerializer
from horario.models import  Horario

class HorarioSet(viewsets.ModelViewSet):
    queryset = Horario.objects.all()
    serializer_class = HorarioSerializer
# Create your views here.
