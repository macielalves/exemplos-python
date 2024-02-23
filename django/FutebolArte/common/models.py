from django.db import models


# Create your models here.
class Pais(models.Model):
    nome = models.CharField(max_length=100)
    continente = models.CharField(max_length=100)

    class Meta:
        verbose_name = "País"
        verbose_name_plural = "Países"

    def __str__(self):
        return self.nome


class Estado(models.Model):
    nome = models.CharField(max_length=100)
    regiao = models.CharField(max_length=100)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Estado"
        verbose_name_plural = "Estados"

    def __str__(self):
        return self.nome


class Cidade(models.Model):
    nome = models.CharField("Nome da cidade", max_length=255)
    populacao = models.PositiveBigIntegerField("População")

    class Meta:
        verbose_name = "Cidade"
        verbose_name_plural = "Cidades"

    def __str__(self):
        return self.nome
