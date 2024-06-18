# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Colyana Magalhães da Silva Nascimento
# Data: 17/06/2024
# Atividade 007: Listas

# E) Faça um programa que receba 7 números inteiros. Depois quebre
# essa lista em: lista de pares e lista de ímpares. 

import os


os.system('cls')

print('-' * 70)
print('Seja bem-vindo ao programa!')
print('Vamos dividir uma lista em duas, em números pares e ímpares.')
print('=' * 70)

lista_numeros = []
lista_pares = []
lista_impares = []

for i in range(1, 8):
    numero = int(input(f'Insira o {i}º número na lista: '))
    lista_numeros.append(numero)
    
for numero in lista_numeros:
    if numero % 2 == 0:
        lista_pares.append(numero)
    else:
        lista_impares.append(numero)
        
print('')
print(f'Lista de números pares: {lista_pares}')
print(f'Lista de números ímpares: {lista_impares}')

print('-' * 70)
print('Fim do programa')
print('')