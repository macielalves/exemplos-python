def aoCubo(n):
    return n**3


def sim_nao(frase="'S' ou 'N': "):
    while True:
        c = input(frase)
        if c == "S":
            print(c)
            return True
        elif c == "N":
            print(c)
            return False
        else:
            print("Caractere Inválido! Digite Novamente!")


while True:
    try:
        n = float(input("Digite um número: "))
        print(aoCubo(n))
        if sim_nao("Deseja continuar? ('S' ou 'N'): "):
            continue
        break
    except ValueError:
        print("\nVerifique o valor inserido e tente novamente!\n")
