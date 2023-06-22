
import random


def gerar_cpf():
    cpf = [random.randint(0, 9) for _ in range(11)]
    cpf_str = ''.join(str(num) for num in cpf)
    return cpf_str


cpf_aleatorio = gerar_cpf()
print(cpf_aleatorio)
