# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Colyana Magalhães da Silva Nascimento
# Data: 14/05/2024
# Atividade 003: Funções/Métodos Internos

# B) Faça um programa que receba 2 valores, faça a divisão entre eles
# . Se a divisão não for inteira, o programa deverá arredondar o 
# resultado para cima e para baixo. Faça a validação para divisão por
# 0.

import os
import math


os.system('cls')

print('-' * 70)
print('ATIVIDADE 3: Questão B')
print('Divisão')
print('=' * 70)

# Recebendo os valores
dividendo = float(input('Insira o dividendo: '))
divisor = float(input('Insira o divisor: '))

# Dividindo os valores
divisao = dividendo / divisor

# Validação
if divisor == 0:
    print(f'Erro: A divisão por zero é inválida.')
elif divisao.is_integer():
    print(f'O resultado de {dividendo} dividido por {divisor} é {divisao}')
else:
    resultado_arredondado_para_cima = math.ceil(divisao)
    resultado_arredondado_para_baixo = math.floor(divisao)
    print(f'O resultado de {dividendo} dividido por {divisor} arredondado para cima é {resultado_arredondado_para_cima}\n',
          f'já o resultado da mesma divisão arredondado para baixo é {resultado_arredondado_para_baixo}.')

print('-' * 70)
print()