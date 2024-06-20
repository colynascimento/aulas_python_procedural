# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Colyana Magalhães da Silva Nascimento
# Data: 17/06/2024
# Atividade 006: Listas

# C) Faça um programa que procure na lista
# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# e produza:

# • O intervalo de 1 até 9
# • O intervalo de 8 até 13
# • Os números pares
# • Os números ímpares
# • Os múltiplos de 2, 3 e 4
# • Lista reversa
# • O produto dos intervalos 5-6 por 11-12

import os


os.system('cls')

print('-' * 70)
print('Seja bem-vindo ao programa!')
print('Vamos procurar elementos especificos de uma lista.')
print('=' * 70)

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print('A lista completa é:')
print(lista)
intervalo_um_ao_nove = lista[0:9]

print('-' * 70)
print('Lista do elemento 1 até o 9:')
print(intervalo_um_ao_nove)

intervalo_oito_ao_treze = lista[7:13]

print('-' * 70)
print('Lista do elemento 8 até o 13:')
print(intervalo_oito_ao_treze)

numeros_pares = []

for i in range(0, len(lista)):
    
    if lista[i] % 2 == 0:
        numeros_pares.append(lista[i])

print('-' * 70)
print('Lista dos elementos pares:')        
print(numeros_pares)

numeros_impares = []

for i in range(0, len(lista)):
    
    if lista[i] % 2 != 0:
        numeros_impares.append(lista[i])
        
print('-' * 70)
print('Lista dos elementos ímpares:')
print(numeros_impares)

multiplos = []

for i in range(len(lista)):
    
    if (lista[i] % 2 == 0) or (lista[i] % 3 == 0) or (lista[i] % 4 == 0):
        multiplos.append(lista[i])
        
print('-' * 70)
print('Lista dos múltiplos de 2, 3 e 4: ')
print(multiplos)

lista_reversa = lista[::-1]

print('-' * 70)
print('Lista na ordem inversa: ')
print(lista_reversa)

intervalo_cinco_seis = lista[5:6]
intervalo_onze_doze = lista[11:12]
produto = 1

for numero in intervalo_cinco_seis:
    produto *= numero
for numero in intervalo_onze_doze:
    produto *= numero

print('-' * 70)
print(f'Produto do intervalo 5-6 com o intervalo 11-12: {produto}')

print('=' * 70)
print('Fim do programa')
print('')