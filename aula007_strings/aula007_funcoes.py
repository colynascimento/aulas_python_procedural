# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Colyana Magalhães da Silva Nascimento
# Data: 21/05/2024
# Aula 007 - Funções String em Python

import os


os.system('cls')

print('-' * 70)
print('Funções String em Python')
print('=' * 70)

frase1 = 'Olá, Mundo!'
quantidade_caracteres = len(frase1) # conta os caracteres
print(f'A frase "{frase1}" contém {quantidade_caracteres} caracteres')
print('.' * 70)

minusculas = frase1.lower() # frase em minúsculo
print(f'Frase original: {frase1}')
print(f'Função lower(): {minusculas}')
print('.' * 70)

maiusculas = frase1.upper() # frase em maiúsculo
print(f'Frase original: {frase1}')
print(f'Função upper(): {maiusculas}')
print('.' * 70)

captalizada = frase1.capitalize() # frase captalizada
print(f'Frase original: {frase1}')
print(f'Função capitalize(): {captalizada}')
print('.' * 70)

frase2 = ' Olá, Mundo '
sem_espacos = frase2.strip() # retirar espaços, antes e depois
print(f'Frase original: {frase2}')
print(f'Função strip(): {sem_espacos}')
print('.' * 70)

substituicao = frase2.replace('Mundo', 'Python') # troca palavra
print(f'Frase original: {frase2}')
print(f'Função replace(): {substituicao}')
print('.' * 70)

lista = frase2.split(',') # separa as palavras de uma string em uma lista
print(f'Frase original:{frase2}')
print(f'Função split(): {lista}')
print('.' * 70)

lista = ['Olá', 'mundo']
juncao = '-'.join(lista) # transforma uma lista em uma string com separador
print(f'Frase original: {lista}')
print(f'Função join(): {juncao}')
print('.' * 70)
print()