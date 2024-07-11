# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Colyana Magalhães da Silva Nascimento
# Data: 11/07/2024
# Atividade 010: Funções

# A) Crie uma função que receba uma lista de números.
# Depois retorne duas listas com os números pares, os
# números ímpares, a quantidade de números pares e a
# quantidade de números ímpares.

import os


os.system('cls')

print('-' * 70)
print('Seja bem-vindo ao programa!')
print('Hoje vamos analisar uma lista de números.')
print('=' * 70)

lista_numeros = list()
lista_pares = list()
lista_impares = list()

for i in range(6):
    numero = int(input('Digite um número para inseri-lo na lista: '))
    lista_numeros.append(numero)
    
def analise_numeros():
    for i in lista_numeros:
        if i % 2 == 0:
            lista_pares.append(i)
        elif i % 2 == 1:
            lista_impares.append(i)
        else:
            print(f'{i} não é um número válido, tente novamente.')
        
        