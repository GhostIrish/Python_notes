def soma_todos(valor):
    lista = []
    for c in range(1, valor + 1):
        lista.append(c)
    somado = sum(lista)
    return somado


numero = int(input("Digite um valor: "))

print(soma_todos(numero))
