# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Colyana Magalhães da Silva Nascimento
# Data: 21/05/2024
# Atividade 004: Strings

# Faça um programa que leia o nome de um aluno e mostre quantas vezes
# a letra 'o' aparece e em que posição ela aparece pela primeira e
# última vez.

import os


os.system('cls')

print('-' * 70)
print('Seja bem-vindo ao programa!')
print('Vamos identificar a quantidade de vezes em que a letra O aparece')
print('no nome do aluno e analisa-lo.')
print('=' * 70)

# Entrada de dados
aluno = input('Insira o nome do aluno: ')

# Processamento
quantidade = aluno.count('o') # Tem que fazer a verificação se não houver O no nome
primeiro_o = aluno.find('o') 
ultimo_o = aluno[::-1].find('o')

# Saída
print(f'A letra O aparece {quantidade} vezes no nome do aluno\n'
      f'O primeiro O aparece no índice {primeiro_o}\n'
      f'O último O aparece no índice {ultimo_o}.\n')

print('-' * 70)