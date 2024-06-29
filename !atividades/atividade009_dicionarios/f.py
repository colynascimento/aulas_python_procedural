# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Colyana Magalhães da Silva Nascimento
# Data: 27/06/2024
# Aula 012 - Estruturas de Dados: Dicionarios

# F) Faça um programa que cadastra 5 tipos de vinho.
# Para os campos deste cadastro tome como referência nome do vinho, tipo, teor alcoólico e safra.

import os


os.system('cls')

print('-' * 70)
print('Seja bem-vindo ao programa!')
print('Vamos catalogar alguns vinhos')
print('=' * 70)
print()

catalogo_vinhos = []


print('Cadastro dos vinhos:\n')

for i in range(5):
    
    novo_vinho = dict()
    
    nome = input('Digite o nome do vinho: ')
    tipo = input('Digite o tipo do vinho: ')
    teor_alcoolico = input('Digite o teor alcoolico do vinho: ')
    safra = input('Digite a safra: ')
    print(f'Vinho {nome} cadastrada no catálogo!\n')
    
    novo_vinho['id'] = i + 1    
    novo_vinho['nome'] = nome
    novo_vinho['tipo'] = tipo
    novo_vinho['teor alcoolico'] = teor_alcoolico
    novo_vinho['safra'] = safra
    
    catalogo_vinhos.append(novo_vinho)
    
print('-' * 70)
print('O resultado do catálogo ficou:')
print('=' * 70)
for vinho_cadastrado in catalogo_vinhos:
    for chave, valor in vinho_cadastrado.items():
        print(f'{chave.capitalize()}: {valor}')
print()