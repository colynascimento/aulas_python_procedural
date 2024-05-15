# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Colyana Magalhães da Silva Nascimento
# Data: 14/05/2024
# Atividade 003: Funções/Métodos Internos

# C) Faça um programa que receba as informações de base e expoente. 
# Calcule a potência.

import os
import math


os.system('cls')

print('-' * 70)
print('ATIVIDADE 3: Questão C')
print('Potência')
print('=' * 70)

# Recebendo as informações
base = int(input('Insira o valor da base: '))
expoente = int(input('Insira o valor do expoente: '))

# Processamento
potencia = math.pow(base, expoente)

# Saída
print(f'O resultado de {base} elevado à potência de {expoente} é {potencia}.')

print('-' * 70)
print()