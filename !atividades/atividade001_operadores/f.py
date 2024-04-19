# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Colyana Magalhães da Silva Nascimento
# Data: 18/04/2024
# Atividade 001 - Operadores aritméticos

# f. Faça um programa que receba um número qualquer e calcule o dobro e o triplo desse número.

import os

os.system('cls')

# Entrada
numero = float(input('Digite um número qualquer: '))

# Processamento
dobro = numero * 2
triplo = numero * 3

# Saída
print(f'O dobro do número {numero} é {dobro}, '
      f'já o triplo do mesmo é {triplo}.')