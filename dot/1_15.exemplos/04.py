# jeito Maciel
MEDIA_DE_APROVACAO = 6.0


def media(*args):
    return sum(args) / len(args)


while True:
    try:
        nota1 = float(input("\nDigite a primeira nota: "))
        nota2 = float(input("Digite a segunda nota: "))
        media_final = media(nota1, nota2)
        if media_final >= MEDIA_DE_APROVACAO:
            print("PARABÉNS! Você foi aprovado!")
            break
        else:
            print("Você foi reprovado!")
            print("Não desista, continue tentando!")
            break
    except ValueError:
        print("\nRevise os valores inseridos e tente novamente!")
