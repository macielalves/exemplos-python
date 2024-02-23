from django.contrib import admin
from .models import Jogador, ClubeTime, Competicao, TituloCompeticao


class JogadorInline(admin.StackedInline):
    model = Jogador


class TituloCompeticaoInline(admin.TabularInline):
    model = TituloCompeticao


@admin.register(ClubeTime)
class ClubeTimeAdmin(admin.ModelAdmin):
    inlines = [JogadorInline, TituloCompeticaoInline]


@admin.register(Competicao)
class CompeticaoAdmin(admin.ModelAdmin): ...


admin.site.register(Jogador)
admin.site.register(TituloCompeticao)
