from math import pow, log
from time import sleep


def juros_compostos(m=0, c=0, i=0, t=0):
    taxa_fixa = i / 100
    # formula -> m = c(1 + taxa_fixa) ** t
    if m == 0 or m == False:
        m = c * (1 + taxa_fixa) ** t
        formatado_m = f'{m:.3f}'
        return formatado_m

    if c == 0 or c == False:
        c = m / (1 + taxa_fixa) ** t
        formatado_c = f'{c:.3f}'
        return formatado_c

    # calcula o valor caso o i não seja dado, fiz usando a lógica
    # usando as regras da matemática para resolução que vi no google
    # a função pow faz a exponenciação de um valor desejado por outro
    # usando a regra da matemática e dividindo o tempo por 1
    # vamos obter a raiz televada ao tempo desejado.
    if i == 0 or i == False:
        divide_categoria_i = m / c
        raiz_categoria_i = pow(divide_categoria_i, 1 / t)
        valor_final_i = raiz_categoria_i - 1
        if valor_final_i >= 0.01 and valor_final_i <= 0.99:
            valor_final_i = valor_final_i * 100

        # comentei essa parte pq no fim não faz diferença o resultado
        # ser 0.01 ou 0.1 por exemplo, a multiplicação por
        # 100 ja é o suficiente.
        # if valor_final_i >= 0.01 and valor_final_i <= 0.099:
        #     valor_final_i = valor_final_i * 100

        return valor_final_i

    # aqui eu ACHO que fiz certo.
    if t == 0 or t == False:
        if i > 1:
            i = i / 1000
        if i >= 0.01 and i <= 0.99:
            i = i / 100
        divide_categoria_t = m / c
        logaritmo1 = log(divide_categoria_t)
        i = 1 + i
        logaritmo2 = log(i)
        valor_final_t = logaritmo1 / logaritmo2
        return round(valor_final_t)


print(juros_compostos(23.600, 20.000, 6, 0))


def linha():
    print('-' * 50)


linha()
print('Calculadora de juros'.center(50))
linha()


while True:
    print('\033[36m')
    menu = """
MENU:
1 - Calcular juros compostos (alpha)
2 - Calcular juros (por enquanto não funcional)
3 - Sair
    """
    print(menu)
    linha()
    opcao = int(input("Digite a opção desejada: "))
    print()

    if opcao == 1:
        linha()
        print('Aviso, o valor que deseja ser calculado deve ser escrito')
        print('com o número 0.')
        linha()
        sleep(1)
        print()
        montante = float(input('Digite o valor do montante: '))
        print()
        capital = float(input("Digite o valor do capital: "))
        print()
        taxa = float(input('Digite o valor da taxa: '))
        print()
        tempo = float(input('Digite o tempo da aplicação: '))
        print()
        sleep(1)
        calculado = juros_compostos(montante, capital, taxa, tempo)

        linha()
        sleep(1)
        if montante == 0:
            print(f'O valor do montante é igual a {calculado}!')

        if capital == 0:
            print(f"O valor do capital aplicado é R${calculado:.2f}.")

        if taxa == 0:
            print(f'A taxa é de {calculado}% ao mês.')

        if tempo == 0:
            print('O tempo da aplicação baseado nas informações')
            print(f'passadas é de {calculado} meses.')
        linha()

    if opcao == 2:
        print("\033[31mERRO, essa opção estara disponivel em breve.")
        sleep(1)

    if opcao == 3:
        print('Ok, até a próxima!')
        sleep(1)
        break

    if opcao not in (1, 2, 3):
        print('\033[31mOpção inválida, digite apenas 1, 2 ou 3!')
