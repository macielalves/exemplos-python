def contar_divisores(n):
    return [1 if n % i == 0 else 0 for i in range(1, n + 1)].count(1)


while True:
    try:
        n = int(input("\nDigite um número: "))
        print("O número %d possui %d divisores." % (n, contar_divisores(n)))
        break
    except ValueError:
        print("\nValor Inválido! Digite Novamente.")
        continue
