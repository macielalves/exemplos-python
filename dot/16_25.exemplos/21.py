def contar_substring(s, sb):
    return sum(1 if s[j - len(sb) : j] == sb else 0 for j in range(len(sb), len(s) + 1))


while True:
    try:
        string = input("\nInsira ou digite um texto: ")
        substring = input("\nDigite uma letra ou palavra: ")
        if not substring.isalpha():
            raise ValueError("Somente letra ou palavra!")
        print(
            '\nA %s "%s" aparece %s vezes no texto.'
            % (
                ("palavra" if len(substring) > 1 else "letra"),
                substring,
                contar_substring(string, substring),
            )
        )
        break
    except ValueError as err:
        print("Valor inválido! %s Digite Novamente." % err)
