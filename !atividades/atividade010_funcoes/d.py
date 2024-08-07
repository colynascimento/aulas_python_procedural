# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Colyana Magalhães da Silva Nascimento
# Data: 11/07/2024
# Atividade 010: Funções

# D) Crie uma função que receba uma temperatura em fahrenheit e retorne o valor em graus célsius.

import os
import time


os.system('cls')

print('-' * 70)
print('Seja bem-vindo ao programa!')
print('Hoje vamos converter graus Fahrenheit para Celsius.')
print('=' * 70)


def conversor_de_temperatura(f):
    c = ((f - 32) / 9) * 5
    return c


fahrenheit = int(input('Digite uma temperatura em Fahrenheit: '))

celsius = conversor_de_temperatura(fahrenheit)

print('\nCalculando...')
time.sleep(1)

print(f'\nA temperatura {fahrenheit}ºF em Celsius é {celsius}ºC')

print()
print('Fim do programa!')
print('-' * 70)