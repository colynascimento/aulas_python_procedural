# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Colyana Magalhães da Silva Nascimento
# Data: 11/06/2024
# Aula 010 - Estruturas de Dados: Métodos e Funções - Saída com In e Not In

import os


os.system('cls')

print('-' * 70)
print('ESTRUTURA DE DADOS: SAÍDA COM IN E NOT IN')
print('=' * 70)

# Exemplo com IN
lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

if(3 in lista_numeros):
    print(lista_numeros)
    posicao = lista_numeros.index(3)
    print(f'O número 3 está na posição {posicao}')
else:
    print('O elemento não consta na listagem')
    
print('')

# Exemplo com Not In
lista_nomes = ['João', 'Jade', 'Carol']

if ('Maria' not in lista_nomes):
    # Antes
    print(lista_nomes)
    
    # Não está na lista, acrescentar
    lista_nomes.append('Maria')
    
    print('\nO nome Maria foi acrescentado')
    print(lista_nomes)
    
print('')
print('-' * 70)
print('Fim do programa')
print('-' * 70)