def somadora(n):
    s = 0
    for i in range(1, n + 1):
        s = s + (i**2 + 1) / (i + 3)
    return s


while True:
    try:
        n = int(input("Digite um numero inteiro positivo: "))
        print("Resultado: %d" % somadora(n))
        break
    except ValueError:
        print("\nValor Inválido! Tente novamente!\n")
