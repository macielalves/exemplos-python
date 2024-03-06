def verificar_quadrado_perfeito(n: int):
    aux = (n) ** (1 / 2)
    return False if int((aux - int(aux)) * 10) else True


print(verificar_quadrado_perfeito(2))
