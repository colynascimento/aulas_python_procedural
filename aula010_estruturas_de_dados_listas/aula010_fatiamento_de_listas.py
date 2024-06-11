# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Colyana Magalhães da Silva Nascimento
# Data: 10/06/2024
# Aula 010 - Estruturas de Dados: Fatiamento de uma Lista

import os


os.system('cls')

print('-' * 70)
print('ESTRUTURA DE DADOS: FATIAMENTO DE UMA LISTA []')
print('=' * 70)

lista_mista = ['a', 'b', 3, 'João', 'e', 500, 'g', 'h']

# Fatiamento do 1º elemento
lista_fatiada1 = lista_mista[0]
# Fatia todos os elementos
lista_fatiada2 = lista_mista[0:]
# Fatia os elementos do índice 0 ao índice 6
lista_fatiada3 = lista_mista[0:6]
# Fatia os elementos do índice 0 ao índice 6 de 2 em 2
lista_fatiada4 = lista_mista[0:6:2]
# Fatia os elementos da direita para esquerda
lista_fatiada5 = lista_mista[::-1]

print(f'Fatia o 1º elemento: {lista_fatiada1}')
print(f'Todos os elementos: {lista_fatiada2}')
print(f'Fatia os elementos do índice 0 ao índice 6: {lista_fatiada3}')
print(
    f'Fatia os elementos do índice 0 ao índice 6 no intervalo de 2 em 2: {lista_fatiada4}')
print(f'Fatia os elementos na ordem inversa: {lista_fatiada5}')

print('-' * 70)
print('Fim do programa!')
print('-' * 70)
