# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Colyana Magalhães da Silva Nascimento
# Data: 27/06/2024
# Aula 012 - Estruturas de Dados: Dicionarios - Lista de Dicionários

# ATENÇÃO!!!!! PROVA    

import os


os.system('cls')

print('-' * 70)
print('Estrutura de Dados: DICIONÁRIO')
print('=' * 70)

# Inicialização do Dicionário e da Lista
elementos = {} # Dicionário
periodica = [] # Lista

# Entrada de Dados
for c in range(2): # Considerando a entrada de 2 elementos
    print(f'ENTRADA DE DADOS: {c + 1}')
    simbolo = str(input('Símbolo do elemento: '))
    nome = str(input('Nome do elemento: '))
    print()
    
    # Adiciona dados ao dicionário
    elementos[simbolo] = simbolo
    elementos[nome] = nome
    
    # Usa append() com copy() para adicionar uma cópia do dicionário à lista
    periodica.append(elementos.copy())
    
print()
print('-' * 70)
print('Elementos na tabela periódica: ')
print(periodica)
print('-' * 70)
print()

# For aninhado para percorrer a lista e o dicionário
print('DETALHES DOS ELEMENTOS:')
for elemento in periodica: # Para cada elemento na lista
    for chave, valor in elementos.items(): # Para cada chave a cada valor do dicionário
        print(f'{chave.capitalize()}: {valor}') # Imprime a chave e o valor de maneira legível
    print('-' * 70) # Linha separadora entre elementos