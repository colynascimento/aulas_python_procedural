# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Colyana Magalhães da Silva Nascimento
# Data: 17/06/2024
# Atividade 006: Listas

# F) Faça um programa que leia 5 nomes, depois imprima estes nomes
# com seus respectivos índices.

import os


os.system('cls')

print('-' * 70)
print('Seja bem-vindo ao programa!')
print('Vamos analisar alguns nomes.')
print('=' * 70)

lista_nomes = []

for i in range(1, 6):
    nome = input(f'Insira o {i}º nome: ')
    lista_nomes.append(nome)
    
print(f'\nA lista ficou assim: {lista_nomes}\n')

for i in range(len(lista_nomes)):
    print(f'O nome {lista_nomes[i]} está no índice {i}')
    
print('-' * 70)
print('Fim do programa!')
print('')