# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Colyana Magalhães da Silva Nascimento
# Data: 17/06/2024
# Atividade 006: Listas

# B) Crie uma lista com 5 números inteiros. Depois imprima a soma
# desses valores.

import os


os.system('cls')

print('-' * 70)
print('Seja bem vindo ao programa!')
print('Vamos criar uma lista e somar seus valores.')
print('=' * 70)

lista = []
soma = 0

for i in range(1, 6):
    elemento = input(f'Insira o {i}º número da lista: ')
    
    if not (elemento.isnumeric()):
        i -= 1
        print('Por favor, insira um número válido.')
    else:
        elemento = float(elemento)
        lista.append(elemento)
        soma += elemento
        
print('')
print(f'Os elementos da lista são {lista}')
print(f'A soma dos valores da lista é {soma}')

print('-' * 70)
print('Fim do programa.')
print('')