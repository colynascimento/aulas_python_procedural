# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Colyana Magalhães da Silva Nascimento
# Data: 18/04/2024
# Atividade 001 - Operadores aritméticos

# c. Faça um programa que peça 4 notas, após a entrada de dados calcular a média das notas digitadas.

import os

os.system('cls')

# Entrada
nota1 = float(input('Digite sua 1ª nota: '))
nota2 = float(input('Digite sua 2ª nota: '))
nota3 = float(input('Digite sua 3ª nota: '))
nota4 = float(input('Digite sua 4ª nota: '))

# Processamento
media_notas = (nota1 + nota2 + nota3 + nota4)/4

# Saída
print(f'A média das 4 notas apresentadas acima é {media_notas}')