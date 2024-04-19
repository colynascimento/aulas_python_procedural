# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Colyana Magalhães da Silva Nascimento
# Data: 18/04/2024
# Atividade 001 - Operadores aritméticos

# e. Faça um programa que receba um número inteiro e mostre o sucessor e antecessor.

import os

os.system('cls')

# Entrada
numero = int(input('Digite um número inteiro: '))

# Processamento
antecessor = numero - 1
sucessor = numero + 1

# Saída
print(f'O antecessor do número {numero} é {antecessor}, '
      f'e o seu sucessor é {sucessor}.')