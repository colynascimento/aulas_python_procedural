# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Colyana Magalhães da Silva Nascimento
# Data: 18/06/2024
# Desafio CRUD

# Construa um código para exemplificar um CRUD.
# Não é permitido funções ou validações try exception.

import os



lista_compras = []

while True:
    
    opcao = ''
    
    os.system('cls')
    
    print(
        '''Seja bem-vindo a Lista de Compras!
        
        Menu:
        1 - Adicionar item
        2 - Editar item
        3 - Visualizar lista
        4 - Remover item
        5 - Sair do Programa
        '''
    )
    
    comando = input('Digite o comando escolhido: ')
    
    while opcao != '0':
        if comando == '1':
            
            os.system('cls')
            
            adicionar_item = input('Digite o item que deseja adicionar: ')
            
            lista_compras.append(adicionar_item)
            
            os.system('cls')
            
            print(f'O item "{adicionar_item}" foi adicionado!')
            
            print()
            print(
                '''
                Menu:
                
                Deseja adicionar mais um item?
                0 - Não, quero voltar ao menu inicial
                1 - Sim, por favor!
                '''
            )
            opcao = input('Digite o comando escolhido: ')
            
        elif comando == '2':
            
            while True:
            
                os.system('cls')
                
                print('Editar lista: ')
                for indice, item in enumerate(lista_compras):
                    numeracao = indice + 1
                    print(f'{numeracao}. {item}')
                
                    editar_item = input('Qual o número do item que deseja editar? ')
                    
                    if not editar_item.isdigit():
                        
                        os.system('cls')
                        
                        print('Por favor, digite apenas números!')
                        continue
                    
                    editar_item = int(editar_item)
                    
                    for indice, item in enumerate(lista_compras):
                        numeracao = indice + 1 
                        
                        if editar_item == numeracao:
                            novo_item = input(f'Escreva o novo item: ')
                            
                            lista_compras[indice] = novo_item
                            
                            print(f'O item {numeracao} foi alterado!')
                            print('Nova lista:')

            # VALIDAÇÃO!
            # O que eu quero verificar?
            # - Se editar_item é um número
            # - Se editar_item é um número válido dentre os itens da lista
            
            # for indice, item in enumerate(lista_compras):
            #     numeracao = indice + 1
            #     if numeracao == editar_item
                