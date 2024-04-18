# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Colyana Magalhães da Silva Nascimento
# Data: 18/04/2024
# Operadores Aritméticos: Ordem de Precedência

import os

os.system('cls')

print('-' * 70)
print('OPERADORES ARITMÉTICOS: Ordem de Precedência')
print('=' * 70)

# Entrada
nota1 = float(input('1ª nota: '))
nota2 = float(input('2ª nota: '))
nota3 = float(input('3ª nota: '))
nota4 = float(input('4ª nota: '))

# Processamento
soma = nota1 + nota2 + nota3 + nota4
media = nota1 + nota2 + nota3 + nota4 / 4
media_correta = (nota1 + nota2 + nota3 + nota4) / 4

# Saída
print('---- Notas ------------')
print(f'Nota1: {nota1} | Nota2:{nota2} |'
      f'Nota3: {nota3} | Nota4:{nota4}')
print('-' * 70)
print(f'Média errada: {media}')
print(f'Média correta: {media_correta}')
print('-' * 70)