from datetime import datetime
from django.db import models


class Jogador(models.Model):
    nome = models.CharField(max_length=255)
    foto = models.ImageField(upload_to="img/gamer")
    clube = models.OneToOneField(
        "ClubeTime", on_delete=models.SET_NULL, blank=True, null=True
    )
    posicao_principal = models.CharField(max_length=255)
    numero_camisa = models.PositiveIntegerField(default=1)
    sexo = models.CharField(
        max_length=1, choices={"M": "Masculino", "F": "Feminino"}, default="M"
    )

    class Meta:
        verbose_name_plural = "Jogadores"

    def __str__(self):
        return self.nome


class ClubeTime(models.Model):
    nome = models.CharField(max_length=255)
    ano_fund = models.PositiveIntegerField("Ano de Fundação")
    divisao_atual = models.CharField(
        max_length=1,
        choices=(
            ("A", "Serie A"),
            ("B", "Serie B"),
            ("C", "Serie C"),
            ("D", "Serie D"),
        ),
        default="A",
    )
    escudo_clube = models.ImageField("Escudo", upload_to="img/shell")
    cidade = models.CharField(max_length=255)
    uf = models.CharField(max_length=255)
    pais = models.CharField("País", max_length=255)
    categoria = models.CharField(
        max_length=1, choices=(("M", "Masculino"), ("F", "Feminino")), default="M"
    )
    jogadores = models.ForeignKey(
        Jogador, on_delete=models.SET_NULL, blank=True, null=True
    )
    titulos = models.ForeignKey(
        "TituloCompeticao", on_delete=models.CASCADE, blank=True, null=True
    )

    class Meta:
        verbose_name = "Clube/Time"
        verbose_name_plural = "Clubes/Times"

    def __str__(self):
        return self.nome


class Competicao(models.Model):
    nome = models.CharField(max_length=255)
    tipo = models.CharField(
        max_length=13,
        choices={
            "ESTADUAL": "ESTADUAL",
            "NACIONAL": "NACIONAL",
            "INTERNACIONAL": "INTERNACIONAL",
        },
        default="ESTADUAL",
    )
    categoria = models.CharField(
        max_length=10,
        choices={"COPA": "COPA", "CAMPEONATO": "CAMPEONATO"},
        default="COPA",
    )

    class Meta:
        verbose_name = "Competição"
        verbose_name_plural = "Competições"

    def __str__(self):
        return self.nome


class TituloCompeticao(models.Model):
    clube = models.ForeignKey(ClubeTime, on_delete=models.CASCADE)
    competicao = models.ForeignKey(Competicao, on_delete=models.CASCADE)
    ano_conquista = models.PositiveIntegerField(
        "Ano da Conquista", default=datetime.now().year
    )
    data_exata = models.DateField(auto_now_add=True)
    titulo = models.CharField(
        max_length=7,
        choices=(("CAMPEAO", "Campeão"), ("VICE", "Vice")),
        default="CAMPEAO",
    )

    class Meta:
        verbose_name = "Título de Competição"
        verbose_name_plural = "Título de Competições"
