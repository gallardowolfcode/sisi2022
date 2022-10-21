from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import viewsets
from .permissions import UserPermission


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    http_method_names = ['get', 'post', 'patch', 'delete']

    permission_classes = (UserPermission)

    filterset_fields = []
    search_fields = ['name', 'email']
    ordering_fields = ['id', 'email', 'name']
    ordering = ['-date_joined']

class ProveedorViewSet(viewsets.ModelViewSet):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class DepartamentoViewSet(viewsets.ModelViewSet):
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer