# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Colyana Magalhães da Silva Nascimento
# Data: 25/06/2024
# Aula 012 - Estruturas de Dados: Dicionarios - Métodos Clear, Copy e Len

import os
import time


os.system('cls')

meu_dicionario = None

# Loop principal do programa
while True:
    print('-' * 70)
    print('\nMenu de opções:')
    print('1. Criar um dicionário com fromkeys()')
    print('2. Buscar o valor de uma chave com get()')
    print('3. Sair')
    print('-' * 70)
    
    opcao = input('Escolha uma opção de (1-3): ')
    
    if opcao == '1':
        chaves = input('Digite as chaves separadas por vírgula: ').split(',')
        valor_padrao = input('Digite o valor padrão para as chaves: ')
        meu_dicionario = dict.fromkeys(chaves, valor_padrao)
        
        print(f'Dicionário criado: {meu_dicionario}')
        time.sleep(3)
        
    elif opcao == '2':
        if meu_dicionario is not None:
            chave = input('Digite a chave que deseja buscar: ')
            valor = meu_dicionario.get(chave, 'Chave não encontrada')
            print(f'Valor para a chave "{chave}": {valor}')
        else:
            print('Erro! Crie um dicionário')
            
    elif opcao == '3':
        print('Saindo do programa...')
        time.sleep(2)
        break
        
    else:
        print('Opção inválida. Tente novamente.')
        time.sleep(3)