def encontra_vogal(string):
    vogais = 'AEIOUaeiou'
    vogais_string = []
    for c in string:
        if c in vogais:
            vogais_string.append(c)
    return vogais_string


frase = str(input("Digite uma frase: "))

vogais = encontra_vogal(frase)
print(vogais)
