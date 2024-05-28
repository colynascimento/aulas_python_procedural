# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Colyana Magalhães da Silva Nascimento
# Data: 28/05/2024
# Aula 008 - For...Range() Continue

import os


os.system('cls')

print('-' * 70)
print('ESTRUTURA DE CONTROLE: CONTINUE')
print('=' * 70)

print()

for var_iteradora in range (1, 11):
    if var_iteradora == 5:
        # 5 está fora do loop, se retirar a linha abaixo, ele não aparecerá na saída
        # a linha abaixo serve apenas para verificação
        print(f'O número {var_iteradora} está fora do loop')
        continue
    print(f'O número é {var_iteradora}')
    
print('-' * 70)
print()