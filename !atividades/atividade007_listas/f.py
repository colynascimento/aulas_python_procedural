# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Colyana Magalhães da Silva Nascimento
# Data: 17/06/2024
# Atividade 007: Listas

# F) Faça um programa que gere 10 números aleatórios. Após gerar
# esses números, crie duas listas novas com ordenação ascendente e
# descendente.

import os
import random


os.system('cls')

print('-' * 70)
print('Seja bem-vindo ao programa!')
print('Vamos criar uma lista aleatória e ordená-la.')
print('=' * 70)

lista_numeros = []

for i in range(10):
    numero = random.randint(-100, 100)
    lista_numeros.append(numero)


lista_crescente = lista_numeros[:]
lista_decrescente = lista_numeros[:]

lista_crescente.sort()
lista_decrescente.sort(reverse=True)
    
print(f'Lista original: {lista_numeros}')
print(f'Lista em ordem ascendente: {lista_crescente}')
print(f'Lista em ordem descendente: {lista_decrescente}')

print('-' * 70)
print('Fim do programa')
print('')