# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Colyana Magalhães da Silva Nascimento
# Data: 17/06/2024
# Atividade 006: Listas

# G) Ler uma lista com 10 números, depois apresente o maior e o menor
# número da lista

import os


os.system('cls')

print('-' * 70)
print('Seja bem-vindo ao programa!')
print('Vamos analisar uma lista com 10 números.')
print('=' * 70)

lista = []

for i in range(1, 11):
    numero = input(f'Insira o {i}º número da lista: ')
        
print(f'A lista final ficou: {lista}')

menor = min(lista)

maior = max(lista)

print(f'O menor número da lista é: {menor}')
print(f'O maior número da lista e: {maior}')

print('-' * 70)
print('Fim do programa!')
print('')