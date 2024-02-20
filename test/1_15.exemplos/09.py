def soma_intervalo(a, b):
    soma = 0
    for i in range(a, b + 1):
        soma += i
    return soma


while True:
    try:
        n1 = int(input("\nDigite o primeiro número: "))
        n2 = int(input("\nDigite o segundo número: "))
        if n1 <= n2:
            print("\nA soma do intervalo informado é ", soma_intervalo(n1, n2))
            break
        else:
            print("\nn2 deve ser maior que n1. Digite novamente!")
    except:
        print("\nValor inválido. Digite novamente!")
