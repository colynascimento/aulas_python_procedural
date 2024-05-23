# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Colyana Magalhães da Silva Nascimento
# Data: 21/05/2024
# Atividade 004: Strings

# Faça um programa que leia uma frase e depois exiba na tela:
# • A frase em minúsculas, a frase em maiúsculas, a quantidade de
# caracteres na frase e quantas letras tem a 2ª palavra na frase.

import os


os.system('cls')

print('-' * 70)
print('Seja bem-vindo ao programa!')
print('Vamos testar algumas funções em Python!')
print('=' * 70)

# Entrada de dados
frase = input('Digite uma frase: ')

# Processamento
minuscula = frase.lower()
maiuscula = frase.upper()
quantia_caracteres = len(frase)
quantia_caracteres_segunda_palavra = len(frase.split()[1])

# Saída
print(f'Sua frase em letras minúsculas usando lower(): {minuscula}\n'
      f'Sua frase em letras maiúsculas usando upper(): {maiuscula}\n'
      f'A frase digitada tem {quantia_caracteres} caracteres.\n'
      f'A segunda palavra da frase tem {quantia_caracteres_segunda_palavra} caracteres.\n'
      )

print('-' * 70)