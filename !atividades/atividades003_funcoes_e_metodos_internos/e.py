# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Colyana Magalhães da Silva Nascimento
# Data: 14/05/2024
# Atividade 003: Funções/Métodos Internos

# E) Faça um programa para sortear um número de 1 a 20.

import os
import random


os.system('cls')

print('-' * 70)
print('ATIVIDADE 3: Questão E')
print('Sorteio de 20')
print('=' * 70)

numero_sorteado = random.randint(1, 20)

print(f'O número sorteado é {numero_sorteado}')
print('-' * 70)
print()
