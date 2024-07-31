# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Colyana Magalhães da Silva Nascimento
# Data: 11/07/2024
# Atividade 010: Funções

# H) Uma Academia deseja fazer uma pesquisa entre seus clientes para
# descobrir a média de altura e peso de seus clientes. Faça um
# programa que pergunte a cada um dos clientes da academia seu código,
# nome, altura e peso. Após esse cadastramento, seu programa deverá
# listar os dados dos clientes e a média. Para sair do programa o
# usuário deverá digitar o valor zero(0). O número de clientes é
# indefinido. Veja a saída no próximo slide.

import os

os.system('cls')


lista_cadastros = list()


def cadastro():
    novo_cadastro = dict()

    novo_cadastro['Matrícula'] = input('Número da matrícula: ')
    novo_cadastro['Nome'] = input('Nome: ')
    novo_cadastro['Altura'] = float(input('Altura: '))
    novo_cadastro['Peso'] = float(input('Peso: '))

    lista_cadastros.append(novo_cadastro)


def exibir_dados():
    for cliente in lista_cadastros:
        for chave, valor in cliente.items():
            print(f'{chave}: {valor}', end='\n')

    media_altura = 0
    media_peso = 0

    for cliente in lista_cadastros:
        for chave, valor in cliente.items():
            if chave == 'Altura':
                media_altura += valor
            elif chave == 'Peso':
                media_peso += valor

    media_altura /= len(lista_cadastros)
    media_peso /= len(lista_cadastros)

    print('+------------------------------------------------+')
    print('|               Média dos Clientes               |')
    print('+------------------------------------------------+')
    print(f'|    Média de altura: {media_altura}                          |')
    print(f'|    Média de peso: {media_peso}                               |')
    print('+------------------------------------------------+')

while True:
    print('+------------------------------------------------+')
    print('|                    ACADEMIA                    |')
    print('|                Área de Cadastro                |')
    print('+================================================+')
    print('|               1 - Novo Cadastro                |')
    print('|               2 - Exibir Clientes              |')
    print('|              0 - Sair do Programa              |')
    print('+------------------------------------------------+')

    opcao = input('|        Digite o comando (0-2): ')

    if opcao == '1':
        cadastro()
    elif opcao == '2':
        exibir_dados()
    elif opcao == '0':
        break
    else:
        print('Comando inválido. Digite apenas 0, 1 ou 2.')
        print('Aperte Enter para continuar...')