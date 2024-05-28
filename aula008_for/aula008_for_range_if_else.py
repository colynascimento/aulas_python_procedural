# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Colyana Magalhães da Silva Nascimento
# Data: 27/05/2024
# Aula 008 - For...Range() com If... Else

import os


os.system('cls')

print('-' * 70)
print('ESTRUTURA DE CONTROLE E IF')
print('=' * 70)

print()

soma = 0

for var_iteradora in range(0, 4):
    numero = int(input(f'{var_iteradora + 1}º número: '))
    
    if(numero % 2 == 0):
        print(f'O número {numero} é par')
    else:
        print(f'O número {numero} é ímpar')
        

print('-' * 70)
print()