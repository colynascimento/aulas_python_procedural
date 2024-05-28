# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Colyana Magalhães da Silva Nascimento
# Data: 27/05/2024
# Aula 008 - For...Range() com Somatório

import os


os.system('cls')

print('-' * 70)
print('ESTRUTURA DE CONTROLE COM SOMATÓRIO')
print('=' * 70)

print()

soma = 0

for var_iteradora in range(0, 4):
    numero = int(input(f'Digite o {var_iteradora + 1}º número: '))
    
    soma += numero
    
print('-' * 70)
print(f'A soma dos números é: {soma}')
print('-' * 70)
print()