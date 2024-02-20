def f(n):
    s = 0
    for i in range(1, n + 1):
        s = s + 1 / i
    return s


while True:
    try:
        n = int(input("Digite um numero inteiro positivo: "))
        print("Resultado: %d" % f(n))
        break
    except ValueError:
        print("\nValor Inválido! Tente novamente!\n")
