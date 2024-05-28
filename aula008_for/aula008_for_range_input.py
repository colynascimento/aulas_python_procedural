# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Colyana Magalhães da Silva Nascimento
# Data: 27/05/2024
# Aula 008 - For...Range() com Input

import os


os.system('cls')

print('-' * 70)
print('ESTRUTURA DE CONTROLE COM RANGE')
print('=' * 70)

print()
 
 # Para cada var_iteradora no alcance de 1 a 5
for var_iteradora in range(1, 5):
    cor = str(input(f'Digite a {var_iteradora}ª cor: '))
    
print()
print()