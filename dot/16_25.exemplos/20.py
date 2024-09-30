def verificar_ano_bisexto(ano):
    return True if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0 else False


while True:
    try:
        ano = int(input("\nDigite um ano: "))
        print(
            "É um ano bisexto" if verificar_ano_bisexto(ano) else "Não é um ano bisexto"
        )
        break
    except ValueError:
        print("Valor inválido! Digite novamente.")
