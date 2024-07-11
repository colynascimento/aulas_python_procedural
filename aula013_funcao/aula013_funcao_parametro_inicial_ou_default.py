# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Colyana Magalhães da Silva Nascimento
# Data: 09/07/2024
# Aula 013 - Funções

import os

# Definição da função
def multiplicar(a, b = 1):
    return a * b

os.system('cls')

resultado_1 = multiplicar(5)
resultado_2 = multiplicar(5, 2)

print('-' * 70)
print('FUNÇÕES: Parâmetro Inicial ou Default')
print('=' * 70)
print()

print(f'Primeiro resultado: {resultado_1}')
print(f'Segundo resultado: {resultado_2}')
print('')
print('-' * 70)