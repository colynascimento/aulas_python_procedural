# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Colyana Magalhães da Silva Nascimento
# Data: 18/04/2024
# Atividade 001 - Operadores aritméticos

# h. Faça um programa que receba um número inteiro, depois imprima sua tabuada de multiplicação.

import os


os.system('cls')

# Entrada
numero = int(input('Digite um número inteiro: '))

# Processamento
tabuada1 = numero * 1
tabuada2 = numero * 2
tabuada3 = numero * 3
tabuada4 = numero * 4
tabuada5 = numero * 5
tabuada6 = numero * 6
tabuada7 = numero * 7
tabuada8 = numero * 8
tabuada9 = numero * 9
tabuada10 = numero * 10

# Saída
print(f'A tabuada do número {numero} é:\n'
      f'{numero} * 1 = {tabuada1}\n'
      f'{numero} * 2 = {tabuada2}\n'
      f'{numero} * 3 = {tabuada3}\n'
      f'{numero} * 4 = {tabuada4}\n'
      f'{numero} * 5 = {tabuada5}\n'
      f'{numero} * 6 = {tabuada6}\n'
      f'{numero} * 7 = {tabuada7}\n'
      f'{numero} * 8 = {tabuada8}\n'
      f'{numero} * 9 = {tabuada9}\n'
      f'{numero} * 10 = {tabuada10}')