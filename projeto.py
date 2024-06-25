# fazer um contador de tarefas no menu
# fazer validação no menu
# opcao de editar tarefas voltar p menu
# tem que ter opcao de remover

import os


os.system('cls')

lista_tarefas = []
adicionar_tarefa = []


while (True):
    opcao = ''
    
    
    os.system('cls')
    print('''
    /~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
    |                  GERENCIADOR DE TAREFAS                  |
    |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
    |                       COMANDOS                           |
    |                                                          |
    | A )=> Adicionar tarefa                                   | 
    | B )=> visualizar tarefa                                  |
    | C )=> Editar tarefa                                      |
    
    |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|''')
    print('    |          Tarefas adicionadas ate o momento: <',len(lista_tarefas),'>        |')
    print('    |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~/')
    comando = str(input('    |Digite seu comando: ')).upper()

    while comando == 'A':
        import os


        os.system('cls')
        print('''
        /~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
        |                       ADICIONAR TAREFA                   |
        |~~~~~~~~~~~~~~~~~~~~~|''')
        adicionar_tarefa = input('    |Insira uma tarefa: ')
        lista_tarefas.append(adicionar_tarefa)
        print('''
        |  Tarefa adicionada! |
        |~~~~~~~~~~~~~~~~~~~~~|''')
        if comando == 'A':
            print('''
        |~~~~~~~~~~~~~~~~~~~~~|
        |       .Opções.      |
        | 0 - Sair            |
        | 1 - Ad. nova tarefa |
        |~~~~~~~~~~~~~~~~~~~~~|''')
            opcao = input('Digite a sua opção: ')
            if (opcao == '0'):
                break

    while comando == 'B':
        import os


        os.system('cls')
        print('''
        |~~~~~~~~~~~~~~~~~~~~~|
        | .Visualizar Tarefas.|
        |~~~~~~~~~~~~~~~~~~~~~| ''')
        
        for indice, tarefa in enumerate(lista_tarefas):
            numeracao = indice + 1
            print(f'{numeracao}. {tarefa}')
        
        print('''
        |~~~~~~~~~~~~~~~~~~~~~|
        | 0 - Sair            |
        |~~~~~~~~~~~~~~~~~~~~~|''')
        opcao = input('Digite a sua opção: ')
        if (opcao == '0'):
            break
    
    while comando == 'C':
        if opcao == '0':
            break
        
        import os


        os.system('cls')
        print('''
        |~~~~~~~~~~~~~~~~~~~~~|
        | .Editar Tarefas.    |
        |~~~~~~~~~~~~~~~~~~~~~| ''')
        for indice, tarefa in enumerate(lista_tarefas):
            numeracao = indice + 1
            print(f'{numeracao}. {tarefa}')
        opcao = input('Digite a tarefa que quer editar: ') 
        # VALIDAÇÃO:
        # - Se o usuário digitou apenas um número OK
        # - Se o número está dentro da lista
        if not opcao.isdigit():
            print('Por favor, digite apenas números.')
            input('Digite qualquer tecla para continuar: ')
            continue

        
        opcao = int(opcao)
        
        for indice, tarefa in enumerate(lista_tarefas):
            numeracao = indice + 1
            # if not opcao == numeracao:
            #     print('Por favor, digite um número válido.')
            #     input('Digite qualquer tecla para continuar: ')
            #     continue
            
            if opcao == numeracao:
                lista_tarefas[indice]= input('Digite a nova tarefa:')
                import os


                os.system('cls')
                print('Tarefa alterada')
                print('''
        |~~~~~~~~~~~~~~~~~~~~~|
        |       .Opções.      |
        | 0 - Sair            |
        | 1 - Ad. nova tarefa |
        |~~~~~~~~~~~~~~~~~~~~~|''')
                opcao = input('Digite a sua opção: ')      
                
# if opcao.isnumeric 