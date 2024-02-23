from django.contrib import admin
from .models import Pais, Estado, Cidade


# Register your models here.
@admin.register(Pais)
class PaisAdmin(admin.ModelAdmin): ...


@admin.register(Estado)
class EstadoAdmin(admin.ModelAdmin): ...


@admin.register(Cidade)
class CidadeAdmin(admin.ModelAdmin): ...
