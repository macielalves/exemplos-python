_PI = 3.14159265358979323846264338327950288419716939937510582097494459230781640628
limPI = len(str(_PI).rstrip("3."))  # Limite de Precisão de PI para esta aplicação
PI = round(_PI, 4)


def get_PI(_p=4):
    if _p <= limPI:
        return round(_PI, _p)
    raise IndexError(f"O limite de precisão é {limPI}")


def volume_esfera(raio, pi=PI):  # 1.1
    return int(4 / 3 * pi * raio**3 * 100) / 100


def volume_esfera_1_(raio):  # 1
    return 4 / 3 * PI * raio**3


def media_escolar(n1, n2, n3, c):  # 2
    if c == "A":
        return (n1 + n2 + n3) / 3
    if c == "P":
        return (n1 * 5 + n2 * 3 + n3 * 2) / 3


def eh_primo(n):  # 3
    if n > 0:
        for i in range(2, n):
            if i % 2 == 0:
                return False
        return True
    # raise ValueError("O valor passado não é positivo!")


def tempo_processo(_s):  # 4
    horas, _minutos = divmod(_s, 3600)
    minutos, _segundos = divmod(_minutos, 60)
    return horas, minutos, _segundos


def converte_idade_em_dias(dias, anos=0, meses=0):  # 5
    dias = dias


def main():
    assert volume_esfera(5) == 523.59
    pass


if __name__ == "__main__":
    main()
