# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Colyana Magalhães da Silva Nascimento
# Data: 17/06/2024
# Atividade 006: Listas

# A) Crie a lista [1, 2, 3, 5, 6] e depois insira o valor que está
# faltando na posição correta.

import os


os.system('cls')

print('-' * 70)
print('Seja bem-vindo ao programa!')
print('Vamos analisar a lista a seguir: ')
print('=' * 70)


lista = [1, 2, 3, 5, 6]
print(lista)
print('')
print('Está faltando um número nessa lista! Vamos corrigir isso.')
print('')

posicao = 2
elemento = 4

lista.insert(posicao, elemento)

print(f'Nova lista: {lista}')
print('Pronto! A lista foi corrigida.')
print('-' * 70)
print('Fim do programa.')
print('')