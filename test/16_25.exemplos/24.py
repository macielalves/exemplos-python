def encontrar_elemento_repetido(numeros):
    # dict_repeticoes = {
    #     str(numeros.count(c)): c for c in numeros
    # }  # <quantidade>:<numero_repetido>
    # return dict_repeticoes[max(dict_repeticoes)]
    # r -> repetições
    r_max = max(r := {str(numeros.count(c)): c for c in numeros})
    return r[r_max]


while True:
    try:
        # lista_ = list(
        #     int(input("add_num: "))
        #     for _ in range(int(input("\nQuantidade de números: ")))
        # )
        lista_ = [6, 5, 4, 3, 3, 2, 1]
        print(encontrar_elemento_repetido(lista_))
        break
    except Exception as err:
        raise err
