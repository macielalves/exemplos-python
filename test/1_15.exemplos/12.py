def somadora(n):
    s = 0
    for i in range(1, n + 1):
        s = s + i
    return s


while True:
    try:
        n = int(input("Digite um numero inteiro positivo: "))
        print("O somatório de %d é %d." % (n, somadora(n)))
        break
    except ValueError:
        print("\nValor Inválido! Tente novamente!\n")
