def lista_pares(lista):
    par = []
    for valor in lista:
        if valor % 2 == 0:
            par.append(valor)
    organizado = sorted(par)
    organizado.reverse()
    return organizado


lista_valores = [3, 8, 12, 7, 5, 6]

print(lista_pares(lista_valores))

frase = str(input("Digite uma frase: ")).upper().strip()

print(frase)
