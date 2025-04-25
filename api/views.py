from django.shortcuts import render
from django.db import models
from rest_framework import generics
from rest_framework.decorators import permission_classes
from rest_framework.response import Response

from Inicio.models import Categoria
from .serializers import CategoriaSerializer


from rest_framework.authentication import TokenAuthentication



class CategoriaListAPIView(generics.ListAPIView):
    serializer_class = CategoriaSerializer


    def get_queryset(self):
        queryset = Categoria.objects.all()
        nombre = self.request.query_params.get('nombre')
        if nombre:
            queryset = queryset.filter(nombre__icontains=nombre)
        return queryset
