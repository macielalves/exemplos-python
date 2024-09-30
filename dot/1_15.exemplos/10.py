def Max(n1, n2):
    if n1 == n2:
        return n1
    elif n1 > n2:
        return n1
    elif n1 < n2:
        return n2


for i in range(4):
    while True:
        try:
            a = float(input("Digite o primeiro número: "))
            b = float(input("Digite o segundo número: "))
            break
        except ValueError:
            print("\nValor Inválido! Tente novamente!\n")
    print("\n%f\n" % Max(a, b))
