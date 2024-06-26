# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Colyana Magalhães da Silva Nascimento
# Data: 25/06/2024
# Aula 011 - Estruturas de Dados: Dicionário - Erros de Digitação

import os


os.system('cls')

print('-' * 70)
print('ESTRUTURA DE DADOS: DICIONÁRIO')
print('=' * 70)

# Índices iguais: só irá exibir um item.
dicionario1 = {'nome': 'João', 'nome': 'Jade'}

# Posso ter uma tupla como índice e uma lista como valor
dicionario2 = {(1, 2): [1, 2]}

# Mas não posso ter uma lista como índice e uma tupla como valor
dicionario3 = {[1, 2]: (1, 2)}

# Saída
print('-' * 70)
print(dicionario1)
print(dicionario2)

print()