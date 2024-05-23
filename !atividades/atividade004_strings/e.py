# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Colyana Magalhães da Silva Nascimento
# Data: 21/05/2024
# Atividade 004: Strings

# E) Faça um programa que receba uma frase e, em seguida, mostre
# quantas vezes as vogais foram utilizadas.

import os


os.system('cls')

print('-' * 70)
print('Seja bem vindo ao programa!')
print('Vamos descobrir quantas vogais tem em uma frase qualquer.')
print('=' * 70)

# Entrada de dados
frase = input('Digite uma frase: ')

# Processamento
vogal_a = frase.count('a')
vogal_e = frase.count('e')
vogal_i = frase.count('i')
vogal_o = frase.count('o')
vogal_u = frase.count('u')
total_vogais = vogal_a + vogal_e + vogal_i + vogal_o + vogal_u

# Saída
print(f'A vogal A aparece {vogal_a} vezes.\n'
      f'A vogal E aparece {vogal_e} vezes.\n'
      f'A vogal I aparece {vogal_i} vezes.\n'
      f'A vogal O aparece {vogal_o} vezes.\n'
      f'A vogal U aparece {vogal_u} vezes.\n'
      f'O número total de vogais na frase é {total_vogais}.\n')

print('-' * 70)