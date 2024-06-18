# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Colyana Magalhães da Silva Nascimento
# Data: 18/06/2024
# Aula 010 - Estruturas de Dados: Métodos e Funções - List Comprehension

import os


os.system('cls')

print('-' * 70)
print('ESTRUTURA DE DADOS: List Comprehensions [ ]')
print('=' * 70)
print('EXEMPLO: Triplicando Valores')
print('')

lista_numeros = [1, 2, 3, 4, 5]

# Triplicar os valores 
lista_nova_triplicada = []

for item in lista_numeros:
    lista_nova_triplicada.append(item * 3)
    
print('Triplicar os valores: forma normal')
print(f'Lista triplicada: {lista_nova_triplicada}')

# List Comprehensions
lista_nova_triplicada2 = [item * 3 for item in lista_numeros]

print('Triplicar os valores: List Comprehensions')
print(f'Lista nova triplicada: {lista_nova_triplicada2}\n')

print('=' * 70)
print('EXEMPLO: Aplicando 10%')
print('')

lista_precos = [100, 200, 300, 500, 600]

# Triplicar os valores
lista_com_juros = []

for item in lista_precos:
    lista_com_juros.append(item + (item * .10))
    
print('Aplicar 10% de juros: forma normal')
print(f'Lista triplicada: {lista_com_juros}')
print()

# List Comprehensions
lista_com_juros2 = [item + (item * .10) for item in lista_precos]
print('Aplicar 10% de juros: List Comprehensions')
print(f'Lista triplicada: {lista_com_juros2}\n')

print('=' * 70)
print('EXEMPLO: Aplicando 10% em Condicional')
print('')

# Triplicar os valores
lista_com_juros3 = []

for valor in lista_precos:
    if valor < 300:
        lista_com_juros3.append(valor + (valor * .10))
    
print('Aplicar juros em condicional: forma normal')
print(f'Lista triplicada: {lista_com_juros3}')
print()

# List Comprehensions
lista_com_juros3 = [valor + (valor * .10)
                    for valor in lista_precos if valor < 300]
print(f'Aplicar juros em condicional: List Comprehensions')
print(f'Lista triplicada: {lista_com_juros3}\n')

print()
print('-' * 70)
print('Fim do Programa')