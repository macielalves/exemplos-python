def contar_caracteres(string):
    return {c: string.count(c) for c in string}


while True:
    try:
        s = input("\nDigite um texto: ")
        print(contar_caracteres(s))
        break
    except Exception as err:
        raise err
