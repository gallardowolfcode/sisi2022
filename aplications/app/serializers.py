from rest_framework import serializers
from django.contrib.auth.models import Group
from .models import *


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

class UserSerializer(serializers.ModelSerializer):

    groups = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
    )

    division = serializers.SlugRelatedField(
        read_only=True,
        slug_field='name'
    )

    class Meta:
        model = User
        exclude = ['password', 'user_permissions']

class UserInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'name', 'email']

class UserCreateSerializer(serializers.ModelSerializer):
    
    extra_kwargs = { 'password': {'write_only': True }}
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'password']

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data.get('password'))
        Departamento = self.context['request'].user.departamento
        user.departamento = Departamento
        user.save()
        user.groups.set(Departamento)
        return user