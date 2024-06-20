import os


os.system('cls')

lista_tarefas = []
adicionar_tarefa = []
opcao = '0'

while (True):
    
    import os
    
    
    os.system('cls')
    
    print('''
    |~~~~~~~~~~~~~~~~~~~~~|
    |......Bem vindo......|
    |~~~~~~Comandos~~~~~~~|
    | A )=> Ad. tarefa    |
    | B )=>vializar tarefa|
    | C )=> Edit. tarefa  |
    |~~~~~~~~~~~~~~~~~~~~~|''')
    comando = str(input('|Digite seu comando: ')).upper()
    print('|~~~~~~~~~~~~~~~~~~~~~|')

    while comando == 'A':
        print('''
        |~~~~~~~~~~~~~~~~~~~~~|
        | .Adicionar Tarefas. |
        |~~~~~~~~~~~~~~~~~~~~~|''')
        adicionar_tarefa = input('|Insira uma tarefa: ')
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
        print('''
        |~~~~~~~~~~~~~~~~~~~~~|
        | .Visualizar Tarefas.|
        |~~~~~~~~~~~~~~~~~~~~~| ''')
        print(lista_tarefas)
        print('''
        |~~~~~~~~~~~~~~~~~~~~~|
        | 0 - Sair            |
        |~~~~~~~~~~~~~~~~~~~~~|''')
        opcao = input('Digite a sua opção: ')
        if (opcao == '0'):
            break

print()