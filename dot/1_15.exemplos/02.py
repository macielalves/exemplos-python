PI = 3.14


def area(r):
    return PI * r**2


def perimetro(r):
    return PI * 2 * r


while True:
    try:
        raio = int(input("\nDigite o raio do círculo: "))
        print("\nA área do círuculo é: %.2f" % area(raio))
        print("\nO perímetro do círculo é %.2f: " % perimetro(raio))
        break
    except ValueError:
        print("\nRevise o valor inserido e tente novamente!")
