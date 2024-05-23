# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Colyana Magalhães da Silva Nascimento
# Data: 21/05/2024
# Atividade 004: Strings

# F) Faça um programa que receba o nome completo de uma pessoa e,
# posteriormente, imprima esse nome separadamente.

import os


os.system('cls')

print('-' * 70)
print('Seja bem-vindo ao programa!')
print('Vamos separar seu nome.')
print('=' * 70)

# Entrada de Dados
nome = input('Insira seu nome completo: ')

# Processamento
nome = nome.split(' ')

# Saída
print(f'Seu nome separado fica assim: {nome}\n')
print('-' * 70)