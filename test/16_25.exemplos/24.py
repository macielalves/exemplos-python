def encontrar_elemento_repetido(numeros):
    # dict_repeticoes = {
    #     str(numeros.count(c)): c for c in numeros
    # }  # <quantidade>:<numero_repetido>
    # return dict_repeticoes[max(dict_repeticoes)]
    # r -> repetições
    r_max = max(r := {str(numeros.count(c)): c for c in numeros})
    return r[r_max]


print(
    encontrar_elemento_repetido(
        [1, 1, 2, 2, 3, 3, 4, 5, 5, 5, 5, 5, 5, 6, 6, 6, 4, 23, 2, 54, 9]
    )
)
