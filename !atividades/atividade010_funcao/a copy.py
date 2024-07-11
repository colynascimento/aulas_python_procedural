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

def pegar_impar_par(lista_numeros):

    lista_pares = list()
    lista_impares = list()
    
    for i in lista_numeros:
        if i % 2 == 0:
            lista_pares.append(i)
        else:
            lista_impares.append(i)
            
    return lista_pares, lista_impares       

lista_numeros = [1, 5, 10, 15]        
pares, impares = pegar_impar_par(lista_numeros)

print(pares)
print(impares)