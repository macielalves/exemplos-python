class Seguro:
    def __init__(self, numero_apolice, proprietario, valor_seguro, valor_premio):
        self._numero_apolice = numero_apolice
        self._proprietario = proprietario
        self._valor_seguro = valor_seguro
        self._valor_premio = valor_premio

    def calculaValor(self):
        pass

    def calculaPremio(self):
        pass


class SeguroVida(Seguro):
    def __init__(
        self,
        numero_apolice,
        proprietario,
        valor_seguro,
        valor_premio,
        idade,
        beneficiario,
    ):
        super().__init__(numero_apolice, proprietario, valor_seguro, valor_premio)
        self._idade = idade
        self._beneficiario = beneficiario

    def calculaValor(self):
        if self._idade <= 30:
            self._valor_seguro = 800
        elif 31 <= self._idade <= 50:
            self._valor_seguro = 1300
        else:
            self._valor_seguro = 1600

    def calculaPremio(self):
        if self._idade <= 30:
            self._valor_premio = 50000
        elif 31 <= self._idade <= 50:
            self._valor_premio = 30000
        else:
            self._valor_premio = 20000


class SeguroAutomovel(Seguro):
    def __init__(
        self,
        numero_apolice,
        proprietario,
        valor_seguro,
        valor_premio,
        numero_licenca,
        modelo,
        ano,
        valor_automovel,
    ):
        super().__init__(numero_apolice, proprietario, valor_seguro, valor_premio)
        self._numero_licenca = numero_licenca
        self._modelo = modelo
        self._ano = ano
        self._valor_automovel = valor_automovel

    def calculaValor(self):
        self._valor_seguro = 0.03 * self._valor_automovel

    def calculaPremio(self):
        self._valor_premio = 0.8 * self._valor_automovel

    def calculaFranquia(self):
        return 0.4 * self._valor_seguro

    class ControleDeSeguros:
        def __init__(self):
            self._seguros = []

        def cadastraSeguro(self, seguro):
            self._seguros.append(seguro)


class Cliente:
    def __init__(self, cpf, nome, idade):
        self.__cpf = cpf
        self.__nome = nome
        self.__idade = idade
        self.seguros = []

    def adiciona_seguro(self, seguro):
        self.seguros.append(seguro)


class ControleDeSeguros:
    def __init__(self):
        self.seguros = []

    def cadastra_seguro(self, seguro):
        self.seguros.append(seguro)

    def relatorio(self):
        for seguro in self.seguros:
            print(
                f"Número da apólice: {seguro._numero_apolice}, Nome do segurado: {seguro._proprietario}, Valor: {seguro._valor_seguro}, Prêmio: {seguro._valor_premio}"
            )
        print(
            f"Total de seguros de vida: {len([seguro for seguro in self.seguros if isinstance(seguro, SeguroVida)])}"
        )
        print(
            f"Total de seguros de automóveis: {len([seguro for seguro in self.seguros if isinstance(seguro, SeguroAutomovel)])}"
        )
        print(
            f"Total dos valores: {sum([seguro._valor_seguro for seguro in self.seguros])}"
        )


cliente = Cliente("123.456.789-00", "João", 35)
seguro_vida = SeguroVida("123", "João", 0, 0, 35, "Maria")
seguro_vida.calculaValor()
seguro_vida.calculaPremio()
cliente.adiciona_seguro(seguro_vida)
seguro_auto = SeguroAutomovel("456", "João", 0, 0, "789", "Fusca", 1972, 10000)
seguro_auto.calculaValor()
seguro_auto.calculaPremio()
cliente.adiciona_seguro(seguro_auto)
controle = ControleDeSeguros()
controle.cadastra_seguro(seguro_vida)
controle.cadastra_seguro(seguro_auto)
controle.relatorio()
