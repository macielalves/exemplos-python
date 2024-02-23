from django.contrib import admin
from .models import Jogador, ClubeTime, Competicao, TituloCompeticao


@admin.register(Jogador)
class JogadorAdmin(admin.ModelAdmin):
    list_display = ["nome"]
    list_filter = ["clube"]


@admin.register(ClubeTime)
class ClubeTimeAdmin(admin.ModelAdmin): ...


@admin.register(Competicao)
class CompeticaoAdmin(admin.ModelAdmin): ...


@admin.register(TituloCompeticao)
class TituloCompeticaoAdmin(admin.ModelAdmin): ...
