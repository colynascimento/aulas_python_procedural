# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Colyana Magalhães da Silva Nascimento
# Data: 10/06/2024
# Aula 010 - Estruturas de Dados: Listas

import os


os.system('cls')

print('-' * 70)
print('ESTRUTURAS DE DADOS: LISTAS []')
print('=' * 70)

lista_numeros_inteiros = [1, 2, 3, 4]
lista_vogais = ['a', 'e', 'i', 'o', 'u']
lista_nomes = ['João', 'Jane', 'Carol']
lista_heterogenea = ['João', 80, 1.90, 'AB']
lista_dentro_da_lista = [[1, 2, 3, 4], ['a', 'e', 'i', 'o', 'u']]

print(f'Lista de números: {lista_numeros_inteiros}')
print(f'Lista de vogais: {lista_vogais}')
print(f'Lista de nomes: {lista_nomes}')
print(f'Lista misturada: {lista_heterogenea}')
print(f'Lista de lista: {lista_dentro_da_lista}')

# Varrendo os índices manualmente
lista_num_indice_0 = lista_numeros_inteiros[0]
lista_vogais_indice_1 = lista_vogais[1]
lista_nomes_indice_2 = lista_nomes[2]
lista_heterogenea_indice_3 = lista_heterogenea[3]
lista_num_indice_1 = lista_dentro_da_lista[1]

print('-' * 70)
print('Acessando os elementos de uma lista')
print('=' * 70)
print(f'Lista de números: {lista_num_indice_0}')
print(f'Lista de vogais: {lista_vogais_indice_1}')
print(f'Lista de nomes: {lista_nomes_indice_2}')
print(f'Lista misturada: {lista_heterogenea_indice_3}')
print(f'Lista de lista: {lista_num_indice_1}')

print('-' * 70)
print('Fim do programa!')
print('-' * 70)
