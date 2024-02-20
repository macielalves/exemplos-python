def fatorial(f):
    fat = 1
    for i in range(1, f + 1):
        fat = fat * i
    return fat


while True:
    try:
        num = int(input("\nDigite um número: "))
        break
    except ValueError:
        print("Valor inválido!")
print("\nO fatorial de %d é: %d" % (num, fatorial(num)))
