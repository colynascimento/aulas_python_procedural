# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Colyana Magalhães da Silva Nascimento
# Data: 11/06/2024
# Aula 010 - Estruturas de Dados: Métodos e Funções - Saída om For... Enumerate

import os


os.system('cls')

print('-' * 70)
print('ESTRUTURA DE DADOS: SAÍDA COM FOR... ENUMERATE()')
print('=' * 70)

soma = 0

# Criando uma lista
lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Percorrendo a lista com enumerate(), o comando enumerate adiciona um índice para cada valor
# de nossa lista start opcional, para não começar no índice 0 enumerate(lista_numeros, start = 1)

# Para cada número dentro da lista de números, enumere com um índice
for indice, numero in enumerate(lista_numeros):
    soma += numero 
    print(f'Indice: {indice} = Número: {numero}')

print('-' * 70)
print(f'A soma de todos os números é: {soma}')
print('Fim do programa!')
print('-' * 70)