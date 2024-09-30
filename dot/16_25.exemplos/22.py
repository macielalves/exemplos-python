from random import randint


def encontrar_elemento_faltante(numeros):
    if numeros:
        for i in range(1, max(numeros)):
            if i not in numeros:
                return i
    return 0


while True:
    try:
        n = int(input("\nDigite um número: "))
        print([i for i in range(1, n + 1)])
        lista_n = [i for i in range(1, n + 1)]
        print("Elemento removido: %d" % lista_n.pop(randint(1, n) - 1))
        elm_ft = encontrar_elemento_faltante(lista_n)
        print(
            "O elemento faltante da lista de 1 a %d é %d"
            % (n, (elm_ft if elm_ft != 0 else n))
        )
        break
    except Exception as err:
        print("Erro %s, Digite novamente!" % err)
