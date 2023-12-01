class ContaCorrente:
    n_acount = 0

    def __init__(self, saldo):
        ContaCorrente.n_acount += 1
        self._numero = ContaCorrente.n_acount
        self._saldo = saldo

    def creditar(self, valor):
        self._saldo += valor
        print(f"[+] Creditamos R$ {valor:.2f} na sua conta")

    def debitar(self, valor):
        if valor <= self._saldo:
            self._saldo -= valor

    @property
    def numero (self):
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
            print(f"[-] Debitamos R$ {valor:.2f} de sua conta")

    def __str__(self):
        return f"Tipo de Conta: Corrente\nNúmero da conta: {self.numero}\nSaldo: {self.saldo}"


class ContaPoupanca(ContaCorrente):
    def __init__(self, saldo, taxa_juros):
        super().__init__(saldo)
        self.taxa_juros = taxa_juros

    def render_juros(self, taxa_juros):
        self._saldo += self._saldo * (taxa_juros/100)

    def __str__(self):
        return f"Tipo de Conta: Poupanca\nNúmero da conta: {self.numero}\nSaldo: {self.saldo}\nTaxa de Juros: {self.taxa_juros}%"


class ContaImposto(ContaCorrente):
    def __init__(self, saldo, percentual_imposto):
        super().__init__(saldo)
        self.percentual_imposto = percentual_imposto

    def calcula_imposto (self):
        self._saldo -= (imposto:=self._saldo * (self.percentual_imposto / 100))
        print(f"Uma taxa de {imposto} foi descontado de seu saldo.")

    def __str__(self):
        return f"Tipo de Conta: Corrente\nNúmero da conta: {self.numero}\nSaldo: {self.saldo}"


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


print(cc1)
print(cc2)
print(cp1)
print(cp2)
print(ci1)
print(ci2)
