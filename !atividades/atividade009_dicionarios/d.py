# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Colyana Magalhães da Silva Nascimento
# Data: 27/06/2024
# Aula 012 - Estruturas de Dados: Dicionarios

# D) Faça um programa para criar um dicionário com 5 cores.
# Depois, imprima as chaves e os valores deste dicionário.

import os


os.system('cls')

print('-' * 70)
print('Seja bem-vindo ao programa!')
print('Vamos catalogar algumas cores')
print('=' * 70)
print()

catalogo_cores = []

print('Cadastro das cores:\n')

for i in range(5):
    
    nova_cor = dict()
    
    cor = input('Digite o nome da cor a ser cadastrada: ')
    print(f'Cor {cor} cadastrada no catálogo!\n')
    
    nova_cor['cor'] = cor
    nova_cor['id'] = i + 1
    
    catalogo_cores.append(nova_cor)
    
print('-' * 70)
print('O resultado do catálogo ficou assim:')
print('=' * 70)
for cor_cadastrada in catalogo_cores:
    for chave, valor in cor_cadastrada.items():
        print(f'{chave.capitalize()}: {valor}')