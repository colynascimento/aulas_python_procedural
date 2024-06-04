# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Colyana Magalhães da Silva Nascimento
# Data: 28/05/2024
# Atividade 005: Estruturas de Controle

# H) Faça um programa que imprima os valores no intervalo definidos 
# pelo usuário.  Defina 3 números que deverão ser ignorados, ou seja,
# que não serão impressos na tela.

import os


os.system('cls')

inicio = int(input('Insira o número inicial: '))
fim = int(input('Insira o número final: '))

for numero in range(inicio, fim):
    if numero == 5 or numero == 37 or numero == 91:
        continue
    else:
        print(numero)