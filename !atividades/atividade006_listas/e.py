# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Colyana Magalhães da Silva Nascimento
# Data: 17/06/2024
# Atividade 006: Listas

# E) Faça um programa que leia as vogais, depois mostre-as em ordem
# inversa.

import os


os.system('cls')

print('-' * 70)
print('Seja bem-vindo ao programa!')
print('Vamos analisar as vogais do nosso alfabeto')
print('=' * 70)

lista_vogais = ['a', 'e', 'i', 'o', 'u']

print(f'As vogais são {lista_vogais}')

# lista_inversa_vogais = lista_vogais[::-1]
lista_vogais.reverse()

print('')
print(f'As vogais na ordem inversa são: {lista_vogais}')

print('-' * 70)
print('Fim do programa!')
print('')