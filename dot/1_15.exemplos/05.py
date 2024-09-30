# requer python version >= 3.10
def peso_ideal(h, s):
    match s:
        case 1:
            return (62.1 * h) - 44.7
        case 2:
            return (72.7 * h) - 58
        case _:
            ...


while True:
    try:
        altura = float(input("\nDigite a altura em metros: "))
        while True:
            try:
                sexo = int(
                    input("\n1 - Feminino\n" "2 - Masculino\n" "Selecione o sexo: ")
                )
                if sexo not in (1, 2):
                    print("\nSelecione somente 1 ou 2!\n")
                    continue
                print("\nSeu peso ideal é %.2fKg" % peso_ideal(altura, sexo))
                break
            except ValueError:
                print("\nValor inválido! Tente novamente!\n")
        break
    except ValueError:
        print("\nVerifique os dados inseridos e tente novamente!")
