def contar_substring(string, substring):
    return string.count(substring)


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
