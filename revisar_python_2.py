def ao_contrario(string):
    palavras = string.split()
    lista_string = []
    for c in palavras:
        lista_string.append(c)
    lista_string.reverse()
    inverso = " ".join(lista_string)
    return inverso


frase = str(input("Digite uma frase: "))

print(ao_contrario(frase))
