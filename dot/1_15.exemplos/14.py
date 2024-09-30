def fatorial(f):
    fat = 1
    for i in range(1, f + 1):
        fat = fat * i
    return fat


def somadora(n):
    s = 0
    for i in range(1, n + 1):
        s = s + 1 / fatorial(i)
    return s


while True:
    try:
        n = int(input("Digite um numero inteiro positivo: "))
        print("Resultado: %d" % somadora(n))
        break
    except ValueError:
        print("\nValor Inválido! Tente novamente!\n")
