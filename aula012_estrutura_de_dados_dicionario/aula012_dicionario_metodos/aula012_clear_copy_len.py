# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Colyana Magalhães da Silva Nascimento
# Data: 25/06/2024
# Aula 012 - Estruturas de Dados: Dicionarios - Métodos Clear, Copy e Len

import os
import time


os.system('cls')
# Criação do dicionário vazio
meu_dicionario = {}

while True:
    print('-' * 70)
    # Exibição do menu opções
    print('\n Menu de opções:')
    print('1. Adicionar um par chave-valor')
    print('2. Mostrar o dicionário')
    print('3. Mostrar o tamanho do dicionário')
    print('4. Fazer uma cópia do dicionário')
    print('5. Limpar o dicionário')
    print('6. Sair')

    # Solicitação da escolha do usuário
    opcao = input('Escolha uma opção de (1-6): ')

    if opcao == '1':
        # Adiciona um novo par chave-valor ao dicionário
        chave = input('Digite a chave: ')
        valor = input('Digite o valor: ')
        meu_dicionario[chave] = valor
        print(f'Par {chave}: {valor} adicionado.')

    elif opcao == '2':
        # Exibe o dicionário atual
        print(f'Dicionário atual: {meu_dicionario}')
        time.sleep(3)

    elif opcao == '3':
        # Mostre o tamanho do dicionário usando len()
        tamanho = len(meu_dicionario)
        print(f'O dicionário tem {tamanho} elementos.')
        time.sleep(3)

    elif opcao == '4':
        # Cria uma cópia do dicionário usando copy() e exibe a cópia
        copia_dicionario = meu_dicionario.copy()
        print(f'Cópia do dicionário: {copia_dicionario}')
        time.sleep(3)

    elif opcao == '5':
        # Limpa o dicionário usando o clear()
        meu_dicionario.clear()
        print('Dicionário limpo.')
        time.sleep(3)

    elif opcao == '6':
        # Sai do programa
        print('Saindo do programa.')
        break

    else:
        # Mensagem para opção inválida
        print('Opção inválida. Tente novamente.')
