from tabnanny import verbose
from unicodedata import name
from unittest.util import _MAX_LENGTH
from django.db import models
from uuid import uuid4
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    id = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=30)
    email = models.EmailField('email', max_length=60)
    phone = models.CharField(unique=True, max_length=16)


class Departamento(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, blank=True, null=True, unique=True)
    email = models.EmailField('email', max_length=60, blank=True, null=True)
    phone = models.CharField(unique=True, max_length=16, blank=True, null=True)

    class Meta:
        verbose_name = 'Mis departamentos'

    def __str__(self):
        return str(self.id) + '-' + self.name + '-' + self.email
    

class Proveedor(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    empresa = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(unique=True, max_length=10)
    email = models.EmailField('email', max_length=60)

    class Meta:
        verbose_name = 'Mis proveedores'

    def __str__(self):
        return str(self.id) + '-' + self.name + '-' + self.empresa
    

class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    cantidad = models.IntegerField(default=0)
    proveedor = models.ForeignKey('proveedor', models.CASCADE, db_column='proveedorid')
    
    class Meta:
        verbose_name = 'Mis productos'

    def __str__(self):
        return str(self.id) + '-' + self.name + '-' + str(self.cantidad)

# class Usuario(models.Model):
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=30)
#     email = models.EmailField('email', max_length=60)
#     phone = models.CharField(unique=True, max_length=16)