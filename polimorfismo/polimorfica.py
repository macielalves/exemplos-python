# -*- coding: utf-8 -*-


class ContaCorrente:
    n_acount = 0

    def __init__(self, saldo):
        ContaCorrente.n_acount += 1
        self._numero = ContaCorrente.n_acount
        self._saldo = saldo

    def creditar(self, valor):
        self._saldo += valor
        print(f"[+] Creditamos R$ {valor:.2f} na conta Nº {self.numero}")

    def debitar(self, valor):
        if valor <= self._saldo:
            self._saldo -= valor

    def sacar(self, valor):
        taxa_saque = 2.00
        if valor <= self._saldo + taxa_saque:
            self._saldo -= valor + taxa_saque
            print(
                f"Conta nº: {self.numero}\nSaque de R$ {valor + taxa_saque:.2f} confirmado"
            )

    @property
    def numero(self):
        return self._numero

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, value):
        self._saldo = value

    def transferir(self, valor, conta):
        if valor <= self._saldo and isinstance(conta, ContaCorrente):
            conta.creditar(valor)
            self._saldo -= valor
            print(f"[-] Debitamos R$ {valor:.2f} da conta Nº {self.numero}")

    def __str__(self):
        return f"Tipo de Conta: Corrente\nNúmero da conta: {self.numero}\nSaldo: {self.saldo}"


class ContaPoupanca(ContaCorrente):
    def __init__(self, saldo, taxa_juros):
        super().__init__(saldo)
        self.taxa_juros = taxa_juros
        self._saques = 5

    @property
    def saques(self):
        return self._saques

    def render_juros(self, taxa_juros):
        self._saldo += self._saldo * (taxa_juros / 100)

    def sacar(self, valor):
        if self._saldo >= valor:
            if self.saques > 1:
                self._saldo -= valor
                self._saques -= 1
                print(f"Conta nº: {self.numero}\nSaque de R$ {valor:.2f} confirmado")
            else:
                taxa_saque = 0.50
                if valor <= self._saldo + taxa_saque:
                    self._saldo -= valor + taxa_saque
                    print(
                        f"Conta nº: {self.numero}\nSaque de R$ {valor + taxa_saque:.2f} confirmado"
                    )

    def __str__(self):
        return f"Tipo de Conta: Poupanca\nNúmero da conta: {self.numero}\nSaldo: {self.saldo}\nTaxa de Juros: {self.taxa_juros}%"


class ContaImposto(ContaCorrente):
    def __init__(self, saldo, percentual_imposto):
        super().__init__(saldo)
        self.percentual_imposto = percentual_imposto

    def calcula_imposto(self):
        self._saldo -= (imposto := self._saldo * (self.percentual_imposto / 100))
        print(f"Uma taxa de {imposto} foi descontado de seu saldo.")

    def __str__(self):
        return f"Tipo de Conta: Imposto\nNúmero da conta: {self.numero}\nSaldo: {self.saldo}"


class Banco:
    __contas = {}

    def __init__(self, nome=""):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    def _num_contas(self):
        return list(self.__contas.keys())

    def adicionar_conta(self, conta):
        self.__contas.update({conta.numero: conta})

    def sacar(self, conta):
        if isinstance(conta, ContaCorrente):
            valor = float(input(f"Saldo: {conta.saldo}\nDigite a quantia: "))
            conta.sacar(valor)
        elif isinstance(conta, (str, int)):
            _conta = self.__contas.get(int(conta))
            if _conta is not None:
                valor = float(input(f"Saldo: {_conta.saldo}\nDigite a quantia: "))
                _conta.sacar(valor)
            else:
                print("Conta não encontrada!")

    def __str__(self) -> str:
        return f"{self.nome}"


cc1 = ContaCorrente(5000)
print(f"Numero: {cc1.numero}\nSaldo: {cc1.saldo}")
cc1.creditar(100)
print(cc1.saldo)
cc1.debitar(2)

cc2 = ContaCorrente(10)
cc1.transferir(50, cc2)

cp1 = ContaPoupanca(200, 1)
cc1.transferir(50, cp1)
cp1.render_juros(12)
cc1.transferir(100, cp1)

cp2 = ContaPoupanca(500, 12)
cc1.transferir(200, cp2)

ci1 = ContaImposto(100000, 1)
cc1.transferir(1, ci1)

ci2 = ContaImposto(1, 1)
cc1.transferir(200, ci2)

banco_Liso = Banco("LisoBank")
contas = [cc1, cc2, cp1, cp2, ci1, ci2]
for conta in contas:
    banco_Liso.adicionar_conta(conta)

banco_Liso.sacar(4000)

print(cc1)
print(cc2)
print(cp1)
print(cp2)
print(ci1)
print(ci2)
