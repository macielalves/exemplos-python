def par_impar(x):
    if x % 2 == 0:
        return True
    else:
        return False


while True:
    try:
        num = int(input("\nDigite um número: "))
        if par_impar(num):
            print("\nO número %d é par." % num)
        else:
            print("\nO número %d é ímpar." % num)
        break
    except ValueError:
        print("\nRevise o valor inserido e tente novamente!")
