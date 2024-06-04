# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Colyana Magalhães da Silva Nascimento
# Data: 28/05/2024
# Atividade 005: Estruturas de Controle

# E) Faça um programa que some a quantidade de números pares 
# encontrados no intervalo entre 0 e 100.

import os


os.system('cls')

pares = 0

for i in range(2, 101, 2):
    pares += 1

print(f'Quantidade de números pares no intervalo de 0 a 100: {pares}')