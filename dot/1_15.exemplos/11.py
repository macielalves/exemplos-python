def contaDivisor(n):
    # quantidade de divisor
    qd = 0
    i = 1
    while i <= n:
        if n % i == 0:
            qd += 1
        i += 1
    return qd


while True:
    try:
        n = int(input("Digite um numero inteiro positivo: "))
        print("%d possui %d divisores" % (n, contaDivisor(n)))
        break
    except ValueError:
        print("\nValor Inválido! Tente novamente!\n")
