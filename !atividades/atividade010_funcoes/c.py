# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Colyana Magalhães da Silva Nascimento
# Data: 11/07/2024
# Atividade 010: Funções

# C) Crie uma função que verifica se uma aluno está
# cadastrado ou não em um dicionário. Se estiver
# cadastrado, imprima o nome desse aluno e o resto dos seus
# dados. O dicionário deverá conter nome, matrícula e a data
# de nascimento do aluno.

import os


os.system('cls')

print('-' * 70)
print('Seja bem-vindo ao programa!')
print('Vamos verificar o cadastro de um aluno.')
print('=' * 70)


def verificar_cadastro(aluno, lista_alunos):

    cadastro = False

    for i in lista_alunos:
        if i == aluno:
            cadastro = True

    if cadastro == False:
        return 'Cadastro não encontrado.'
    else:
        return f"""\nCadastro encontrado: \nNome: {aluno['Nome']}
Data de nascimento: {aluno['Data de nascimento']}
Matrícula: {aluno['Matricula']}"""


lista_alunos = [{'Nome': 'Colyana', 'Data de nascimento': '15/03/2000', 'Matricula': '817147'},
                {'Nome': 'Italo', 'Data de nascimento': '27/04/1990', 'Matricula': '237954'},
                {'Nome': 'Alex', 'Data de nascimento': '29/08/1987', 'Matricula': '657109'}]

# aluno = {'Nome': 'Colyana', 'Data de nascimento': '15/03/2000', 'Matricula': '817147'}
aluno = dict()
aluno['Nome'] = input("Digite o nome do aluno: ").capitalize()
aluno['Data de nascimento'] = input('Digite a data de nascimento do aluno [dd/mm/aaaa]: ' )
aluno['Matricula'] = input('Digite o número de matrícula do aluno: ')

print(verificar_cadastro(aluno, lista_alunos))

print()
print('Fim do programa!')
print('-' * 70)