# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Colyana Magalhães da Silva Nascimento
# Data: 27/06/2024
# Aula 012 - Estruturas de Dados: Dicionarios

# E) Faça um programa para criar um dicionário com 5 ferramentas.
# Depois, imprima os valores e a quantidade de elementos do dicionário.

import os


os.system('cls')

print('-' * 70)
print('Seja bem-vindo ao programa!')
print('Vamos catalogar algumas ferramentas')
print('=' * 70)
print()

catalogo_ferramentas = []
quantidade = 0

print('Cadastro das ferramentas:\n')

for i in range(5):
    
    nova_ferramenta = dict()
    
    ferramenta = input('Digite o nome da ferramenta a ser cadastrada: ')
    print(f'Ferramenta {ferramenta} cadastrada no catálogo!\n')
    
    nova_ferramenta['ferramenta'] = ferramenta
    nova_ferramenta['id'] = i + 1
    
    quantidade += 1
    
    catalogo_ferramentas.append(nova_ferramenta)
    
print('-' * 70)
print('O resultado do catálogo ficou assim:')
print('=' * 70)
for ferramenta_cadastrada in catalogo_ferramentas:
    for chave, valor in ferramenta_cadastrada.items():
        print(f'{chave.capitalize()}: {valor}')
        
print(f'\n Quantidade de ferramentas no catálogo: {quantidade}')