def remover_vogais(s: str):
    # for i in ("a", "A", "e", "E", "i", "I", "o", "O", "u", "U"):
    #     s = s.replace(i, "")
    # return s
    return "".join(["" if c.lower() in "aeiou" else c for c in s])


print(remover_vogais("Author: Maciel Aves; Email: macielalves.dev@gmail.com"))
