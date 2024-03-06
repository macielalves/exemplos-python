def verificar_quadrado_perfeito(n: int):
    aux = (n) ** (1 / 2)
    return False if int((aux - int(aux)) * 10) else True


while True:
    try:
        x = verificar_quadrado_perfeito(int(input("\nDigite um número: ")))
        if x:
            print("É um quadrado perfeito!")
        else:
            print("Não é um quadrado perfeito!")
        break
    except Exception as err:
        raise err
