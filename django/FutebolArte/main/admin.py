from django.contrib import admin
from .models import Jogador, ClubeTime, Competicao, TituloCompeticao
from django.utils.html import format_html


class JogadorInline(admin.StackedInline):
    model = Jogador
    extra = 0


class TituloCompeticaoInline(admin.StackedInline):
    model = TituloCompeticao
    extra = 0


@admin.register(ClubeTime)
class ClubeTimeAdmin(admin.ModelAdmin):
    list_display = [
        "escudo_img",
        "nome",
        "cidade",
        "ano_fund",
        "divisao_atual",
        "ver_detalhes",
    ]
    list_display_links = ["nome", "ver_detalhes"]
    # autocomplete_fields = ["cidade"]
    list_filter = ["divisao_atual"]
    search_fields = ["nome", "cidade__nome"]

    inlines = [JogadorInline, TituloCompeticaoInline]

    @admin.display(description="Escudo")
    def escudo_img(self, obj):
        url = "https://placehold.co/60"
        if obj.escudo_clube:
            url = obj.escudo_clube.url
            print(url)

        return format_html(f'<img src="{url}" width="60" />')

    def ver_detalhes(self, obj):
        return format_html("<p style='color: blue'>Ver Detalhes</p>")


@admin.register(Competicao)
class CompeticaoAdmin(admin.ModelAdmin): ...


# admin.site.register(Jogador)
# admin.site.register(TituloCompeticao)
