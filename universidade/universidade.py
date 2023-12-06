# -*- coding: utf-8 -*-
# Contribuintes: Maciel Alves Pereira, Samuel Alves de Sousa


def no_acess():
    print("Acesso não autorizado!")


class Professor:
    def __init__(self, matricula, nome, titulacao, salario_base):
        self.__matricula = matricula
        self.__nome = nome
        self.__titulacao = titulacao  # 1- Especialista, 2- Mestre ou 3- Doutor.
        self.__dependentes = []
        self.__salario_base = salario_base

        if self.__titulacao in (1, "Especialista"):
            self.__perc_titulacao = 10 / 100
        elif self.__titulacao in (2, "Mestre"):
            self.__perc_titulacao = 20 / 100
        elif self.__titulacao in (3, "Doutor"):
            self.__perc_titulacao = 40 / 100
        else:
            self.__perc_titulacao = 0

    @property
    def matricula(self):
        return self.__matricula

    @matricula.setter
    def matricula(self):
        no_acess()

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, _v):
        no_acess()

    @property
    def titulacao(self):
        return self.__titulacao

    @titulacao.setter
    def titulacao(self, _v):
        no_acess()

    @property
    def dependentes(self):
        list_depend = []
        for depend in self.__dependentes:
            list_depend.append((depend.ano_nasc, depend.nome, depend.parentesco))
        return list_depend

    @dependentes.setter
    def dependentes(self, _v):
        no_acess()

    @property
    def q_dep(self):
        l_dep = []
        for dep in self.__dependentes:
            if dep.calcula_idade(2023) < 7:
                l_dep.append(dep)
        return len(l_dep)

    @property
    def titulacao(self):
        return self.__titulacao

    @titulacao.setter
    def titulacao(self, _v):
        no_acess()

    @property
    def salario_base(self):
        return self.__salario_base

    @salario_base.setter
    def salario_base(self, _v):
        no_acess()

    @property
    def perc_titulacao(self):
        return self.__perc_titulacao

    @perc_titulacao.setter
    def perc_titulacao(self, _v):
        no_acess()

    def adiciona_Dependente(self, dependente):
        self.__dependentes.append(dependente)

    def calcula_salario(self):
        return (
            self.salario_base
            + (self.salario_base * self.perc_titulacao)
            + (self.q_dep * 100)
        )

    @property
    def tipo(self):
        return self.__class__.__name__

    def __str__(self):
        return f"Matricula: {self.matricula}\nNome: {self.nome}\nTitulação: {self.titulacao}"
        # return f"{type(self)}"


class Dependente:
    def __init__(self, ano_nasc, nome, parentesco):
        self.__nome = nome
        self.__ano_nasc = ano_nasc
        self.__parentesco = parentesco

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, _v):
        no_acess()

    @property
    def ano_nasc(self):
        return self.__ano_nasc

    @ano_nasc.setter
    def ano_nasc(self, _v):
        no_acess()

    @property
    def parentesco(self):
        return self.__parentesco

    @parentesco.setter
    def parentesco(self, _v):
        no_acess()

    def calcula_idade(self, ano_atual):
        return ano_atual - self.__ano_nasc


class Horista(Professor):
    def __init__(self, matricula, nome, titulacao, salario_base, carga_horaria):
        super().__init__(matricula, nome, titulacao, salario_base)
        self.__carga_horaria = carga_horaria

    @property
    def carga_horaria(self):
        return self.__carga_horaria

    def calcula_salario(self):
        return super().calcula_salario() + (self.carga_horaria * 20)


class Gratificação:
    def __init__(self, id, descricao, valor):
        self.__id = id
        self.__descricao = descricao
        self.__valor = valor

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, _id):
        no_acess()

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, _v):
        no_acess()

    @property
    def valor(self):
        return self.__valor

    @valor.setter
    def valor(self, _v):
        no_acess()


class Tempo_Integral(Professor):
    def __init__(self, matricula, nome, titulacao, salario_base, tipo_gratificacao):
        super().__init__(matricula, nome, titulacao, salario_base)
        self.__tipo_gratificacao = tipo_gratificacao

    @property
    def tipo_gratificacao(self):
        return self.__tipo_gratificacao

    def calcula_salario(self):
        return super().calcula_salario() + (
            self.tipo_gratificacao.valor * self.salario_base
        )


class Universidade:
    def __init__(self, nome, professores: list[Professor] = []):
        self.__nome = nome
        self.__professores = professores

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, _v):
        no_acess()

    @property
    def professores(self):
        return self.__professores

    @professores.setter
    def professores(self, _v):
        no_acess()

    def adiciona_professor(self, professor):
        self.__professores.append(professor)

    def __str__(self):
        a = f"{' Relatório de professores ':=^65}"
        b = f"Universidade: {self.nome}"
        c = f"{'='*65}"
        d = f"{'matricula':<15}{'Nome':<10}{'tipo':<15}{'Salario':<10}\n"
        total = 0
        total_horista = 0
        total_integral = 0
        for prof in self.__professores:
            d += f"{prof.matricula:<15}{prof.nome:<10}{prof.tipo:<15}{(saldo:=prof.calcula_salario()):<10,.2f}\n"
            if prof.tipo == "Horista":
                total_horista += saldo
            elif prof.tipo == "Tempo_Integral":
                total_integral += saldo
            total += saldo
        e = f"Total .....................................: {f'{total:,.2f}'}"
        f = f"Total pago a professores horistas: {total_horista:,.2f}"
        g = f"Total pago a professores Tempo_Integral: {total_integral:,.2f}"
        return f"{a}\n{b}\n{c}\n{d}\n{c}\n{e}\n{f}\n{g}\n"


g1 = Gratificação(1, "20h", 20 / 100)
g2 = Gratificação(2, "40h", 40 / 100)
g3 = Gratificação(3, "DE", 60 / 100)
prof1 = Horista(1001, "João", 2, 2500, 18)  # matricula, nome, titulação, horas_aula
prof1.adiciona_Dependente(Dependente(2015, "Ana Flávia", "filho(a)"))
prof1.adiciona_Dependente(Dependente(2020, "Bruno", "filho(a)"))
prof1.adiciona_Dependente(Dependente(2022, "Teo", "filho(a)"))
prof2 = Tempo_Integral(
    1002, "Maria", 3, 4000, g2
)  # matricula, nome, titulação, gratificação
prof2.adiciona_Dependente(Dependente(2019, "Cleo", "filho(a)"))
prof2.adiciona_Dependente(Dependente(2016, "Alan", "filho(a)"))
print(prof1.calcula_salario())
# retorna: 2500 + 2500*(20/100) + 2*100 + 18*20 = 3560,00
print(prof2.calcula_salario())
# retorna: 4000 + 4000*40/100 + 1*100 + (40/100)*4000 = 7300,00

prof3 = Tempo_Integral(1003, "José", 3, 5000, g3)
prof3.adiciona_Dependente(Dependente(2015, "Renata", "filho(a)"))
print(prof3.calcula_salario())
# retorna 5000 + 5000*(40/100) + 0*100 + 5000*(60/100) = 10.000,00

ufpi = Universidade("UFPI")
ufpi.adiciona_professor(prof1)
ufpi.adiciona_professor(prof2)
ufpi.adiciona_professor(prof3)

print(ufpi)
# =============== Relatório de professores =====================
# Universidade: UFPI
# ==============================================================
# matricula        Nome        tipo            Salario
# 1001              João        Horista         3.560,00
# 1002              Maria       Tempo_Itegral   7.300,00
# 1003              José        Tempo_Integral  10.000,00
# ==============================================================
# Total .....................................: 20.860,00
# Total pago a professores horistas: 3.560,00
# Total pago a professores Tempo_Integral: 17.300,00

print(prof1.dependentes)
ifpi = Universidade("IFPI")
print(ifpi)
print("Oi")
