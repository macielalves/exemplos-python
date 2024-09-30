def e_primo(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def encontrar_primos_gemeos(n):
    primos_gemeos = []
    for i in range(2, n):
        if e_primo(i) and e_primo(i + 2):
            primos_gemeos += [(i, i + 2)]
    return primos_gemeos


while True:
    try:
        n = int(input("\nDigite um número: "))
        if n > 1:
            print("\nOs primos gemeos entre 1 e %d são:" % n)
            for i in encontrar_primos_gemeos(n):
                # print("(%d, %d)" % (i[0], i[1]))
                print(i)
        break
    except ValueError:
        print("Valor inválido! Digite Novamente.")
    except Exception:
        raise Exception
