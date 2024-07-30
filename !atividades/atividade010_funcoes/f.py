# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Colyana Magalhães da Silva Nascimento
# Data: 30/07/2024
# Atividade 010: Funções

# F) Crie uma função que receba 2 listas: 
# - lista 1: nome, peso, idade
# - lista 2: John, 40, 1.8
# - Sua função deverá criar um dicionário contendo chave e valor
# utilizando como base essas duas listas. Depois, seu programa
# deverá imprimir esse dicionário utilizando uma estrutura de
# repetição for.

import os


os.system('cls')

print('-' * 70)
print('Seja bem-vindo ao programa!')
print('Vamos criar um dicionário mesclando duas listas.')
print('=' * 70)


def criar_dicionario(keys, values):
    dicionario = dict(zip(keys, values))
    return dicionario


chaves = ['Nome', 'Peso', 'Altura']
valores = ['Coly', 50, 1.63]

print(criar_dicionario(chaves, valores))

print()
print('Fim do programa!')
print('-' * 70)