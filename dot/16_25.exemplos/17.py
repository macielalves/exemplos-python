def verificar_anagrama(s1, s2):
    s1, s2 = s1.upper(), s2.upper()
    for i in s1:
        if s1.count(i) == s2.count(i):
            continue
        return False
    return True


while True:
    try:
        s1 = input("\nDigite uma palavra: ")
        s2 = input("\nDigite outra palavra: ")
        if verificar_anagrama(s1, s2):
            print('A palavra "%s" é anagrama de "%s".' % (s1, s2))
        else:
            print('A palavra "%s" não é anagrama de "%s".' % (s1, s2))
        break
    except Exception as err:
        print("Deu ruim! erro %s" % err)
        break
