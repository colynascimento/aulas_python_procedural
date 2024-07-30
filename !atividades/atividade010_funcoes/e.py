# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Colyana Magalhães da Silva Nascimento
# Data: 11/07/2024
# Atividade 010: Funções

# E) Crie uma função que receba a altura e o peso de uma pessoa. Depois retorne o seu IMC.

import os
import time

os.system('cls')

print('-' * 70)
print('Seja bem-vindo ao programa!')
print('Vamos fazer um calculo de IMC.')
print('=' * 70)


def calculo_imc(altura, peso):
    imc = peso / altura ** 2
    return imc


altura = float(input('Digite a altura em metros: '))
peso = float(input('Digite o peso em kg: '))

print('\nCalculando...')
time.sleep(1)

print(f'Seu IMC é {calculo_imc(altura, peso):.2f}')

print()
print('Fim do programa!')
print('-' * 70)
