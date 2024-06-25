# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Colyana Magalhães da Silva Nascimento
# Data: 24/06/2024
# Aula 010 - Estruturas de Dados: Tuplas

import os


os.system('cls')

nomes = ['Ágata', 'Bia', 'Coly', 'Isis']

for indice, nome in enumerate(nomes):
    # cria uma tupla contendo o índice e o nome da pessoa atual
    minha_tupla = (indice, nome)
    # a variável minha_tupla é utilizada para acessar o índice e o 
    # nome armazenado na tupla. Mas posso acessar diretamente os
    # elementos "índice" e "nome".
    print(f'O nome "{minha_tupla[1]}", a posição {minha_tupla[0]} da lista.')
    print(f'O nome "{nome}", a posição {indice} da lista.')
    print('-' * 70)