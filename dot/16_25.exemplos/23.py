def remover_vogais(s: str):
    # for i in ("a", "A", "e", "E", "i", "I", "o", "O", "u", "U"):
    #     s = s.replace(i, "")
    # return s
    return "".join(["" if c.lower() in "aeiou" else c for c in s])


while True:
    try:
        s = input("\nDigite um texto/frase: ")
        print('Sem vogais:\n\t"%s"' % remover_vogais(s))
        break
    except Exception as err:
        raise err
