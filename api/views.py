from django.shortcuts import render
from django.db import models
from rest_framework import viewsets
from rest_framework.decorators import permission_classes
from rest_framework.response import Response

from Inicio.models import Categoria
from .serializers import CategoriaSerializer



class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
