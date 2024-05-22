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
nome = input('Insira o seu nome: ').capitalize()
nome_do_meio = input('Insira o seu nome do meio:').capitalize()
ultimo_nome = input('Insira o seu último nome: ').capitalize()

# Processamento
lista_nome_completo = [nome, nome_do_meio, ultimo_nome]
nome_completo = ' '.join(lista_nome_completo)

# Validação e Saída
if (nome.isnumeric() or nome_do_meio.isnumeric() or ultimo_nome.isnumeric()):
    print('Os caracteres numéricos são inválidos nos campos acima.')
else:
    print(f'O nome seu nome completo é: {nome_completo}')