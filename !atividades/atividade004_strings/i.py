# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Colyana Magalhães da Silva Nascimento
# Data: 21/05/2024
# Atividade 004: Strings

# I) Faça um programa que receba o nome completo de uma pessoa e, em
# seguida, mostre o primeiro e o último nome.

import os


os.system('cls')

print('-' * 70)
print('Seja bem-vindo ao programa!')
print('Vamos isolar apenas o primeiro e o último nome inseridos.')
print('=' * 70)

# Entrada de dados
nome_completo = input('Insira o seu nome completo: ')

# Validação
lista_caracteres_especiais = ['@', '#', '$', '&', '*']

# Processamento
lista_nome_completo = nome_completo.split(' ')
primeiro_nome = lista_nome_completo[0]
indice_ultimo_nome = len(lista_nome_completo) - 1
ultimo_nome = lista_nome_completo[indice_ultimo_nome]

# Saída
if nome_completo in lista_nome_completo:
      print('Os caracteres inseridos são inválidos, por favor use apenas letras.')
else:
      print(f'O primeiro nome é {primeiro_nome}\n'
            f'e o último nome é {ultimo_nome}\n')

print('-' * 70)