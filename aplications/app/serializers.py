from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = []
        
class ProveedorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Proveedor
        fields = ['id', 'name', 'empresa', 'phone', 'email']

class ProductoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Producto
        exclude=[]

class DepartamentoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Departamento
        exclude=[]
