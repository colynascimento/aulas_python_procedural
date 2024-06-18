# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Colyana Magalhães da Silva Nascimento
# Data: 17/06/2024
# Atividade 007: Listas

# B) Faça um programa que preencha uma lista com 50 números
# aleatórios. Depois fatie essa lista em 5 listas de 10 elementos.

import random
import os


os.system('cls')

print('-' * 70)
print('Seja bem-vindo ao programa!')
print('Vamos analisar listas numéricas aleatórias.')
print('=' * 70)

lista_numeros = []

for i in range(50):
    numero = random.randint(-1000, 1000)
    
    lista_numeros.append(numero)

lista1 = lista_numeros[0:10]
lista2 = lista_numeros[10:20]
lista3 = lista_numeros[20:30]
lista4 = lista_numeros[30:40]
lista5 = lista_numeros[40:50]
    
print('Foram geradas 5 listas de 10 elementos cada!')
print('')
print(f'Lista 1: {lista1}')
print(f'Lista 2: {lista2}')
print(f'Lista 3: {lista3}')
print(f'Lista 4: {lista4}')
print(f'Lista 5: {lista5}')

print('-' * 70)
print('Fim do programa')
print('')