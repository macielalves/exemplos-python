def calculo_de_poligono(nlados, tlado):
    """Calcula o perímetro se a quantidade de lados for 3, calcula a área se a
    quantidade de lados for 4.
    Args:
        nlados ( int | float ): número de lados. Escolha 3, 4 ou 5.
        tlado ( int | float ): tamanho do lado. O valor do lado do polígono é em centímetros.
    """
    if nlados == 3:
        print("TRIÂNGULO, perímetro %.2fcm" % (r := (nlados * tlado)))
        return
    elif nlados == 4:
        print("QUADRADO, área %.2fcm²" % (r := (tlado**2)))
        return
    elif nlados == 5:
        print("PENTÁGONO")
        return


while True:
    try:
        nlados = int(input("Selecione o número de lados (3, 4 ou 5): "))
        if nlados not in (3, 4, 5):
            print("\nOs valores permitidos são 3, 4 ou 5!\n")
            continue
        while True:
            try:
                tlado = float(input("Informe o tamanho do lado (em centímetros): "))
                break
            except ValueError as err:
                print("Valor inválido '%s'!" % err.__str__().split("'")[1])
        calculo_de_poligono(nlados, tlado)
    except ValueError as err:
        try:
            print("Valor inválido '%s'!" % err.__str__().split("'")[1])
            continue
        except Exception as err:
            raise err
    break
