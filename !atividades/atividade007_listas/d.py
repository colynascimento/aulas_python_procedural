# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Colyana Magalhães da Silva Nascimento
# Data: 17/06/2024
# Atividade 007: Listas

# D) Crie uma lista com 6 nomes, depois verifique se o nome ‘Pedro’ está nessa lista.

import os


os.system('cls')

print('-' * 70)
print('Seja bem-vindo ao programa!')
print('Vamos fazer uma lista e analisar.')
print('=' * 70)

lista_nomes = []

for i in range(6):
    nome = input('Insira um nome na lista:')
    lista_nomes.append(nome)

print('')

if ('Pedro' in lista_nomes):
    print(f'O nome do Pedro está na lista!')
else:
    print(f'O nome do Pedro não está na lista.')
    
print('-' * 70)
print('Fim do programa.')
print('')    