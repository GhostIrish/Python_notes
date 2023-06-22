# from datetime import date, datetime

# data_atual = date.today()

# hora = datetime.now()
# hora_str = hora.strftime('%d')
# print(hora.date())


# ______________________________________________________________________________________

# Considere o seguinte dicionário: {'m1': {'m2': 'Olá Mundo'}}.
# Carregue e apresente a mensagem "Olá Mundo" contida no dicionário

# dicionario = {'m1': {'m2': 'Ola mundo'}}

# print(dicionario['m1']['m2'])


# ______________________________________________________________________________________

# Desenvolva um programa que tenha uma função que verifique se um número
# inteiro qualquer é par ou impar


# def verificador(x):
#     if x % 2 == 0:
#         return 'Esse valor é par'
#     else:
#         return 'Esse valor é ímpar'


# print(verificador(4))

# ______________________________________________________________________________________

# Desenvolva um programa que armazene quatro notas em uma lista
# e que apresente: a média final, a maior nota e a menor nota

# notas = []

# for c in range(0, 4):
#     nota = float(input(f"Digite a nota {c + 1}º: "))
#     notas.append(nota)

# def media(lista):
#     media_lista = sum(lista) / len(lista)
#     if media_lista >= 7:
#         return f'APROVADO com média {media_lista}'
#     else:
#         return f'REPROVADO com média {media_lista}'


# print(media(notas))

# print(max(notas))
# print(min(notas))

# _______________________________________________________________________________________

# Desenvolva um programa que altere em tempo de execução a palavra Java pela
# palavra Python na frase Exercícios de Java

frase = 'Exercicios de Java'.upper()

if 'JAVA' in frase == True:
    alterado = frase.replace('java', 'Python')
    print(alterado.capitalize())
else:
    print(frase.capitalize())
