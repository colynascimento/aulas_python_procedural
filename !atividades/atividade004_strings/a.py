# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Colyana Magalhães da Silva Nascimento
# Data: 21/05/2024
# Atividade 004: Strings

# A) Faça um programa que solicite separadamente o nome, o nome do
# meio e o sobrenome de uma pessoa. Em seguida, imprima o nome 
# completo.

import os


os.system('cls')

# Entrada de dados
nome = input('Insira o seu nome: ')
nome_do_meio = input('Insira o seu nome do meio:')
ultimo_nome = input('Insira o seu último nome: ')

# Validação
if (nome.isnumeric() or nome_do_meio.isnumeric() or ultimo_nome.isnumeric()):
    print('Os caracteres numéricos são inválidos nesses campos.')
else:
    print('oi')