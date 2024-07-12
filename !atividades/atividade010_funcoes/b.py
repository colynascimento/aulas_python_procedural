# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Colyana Magalhães da Silva Nascimento
# Data: 11/07/2024
# Atividade 010: Funções

# B) Crie uma função que cadastre o nome de um aluno, a 
# matrícula e a data de nascimento. Depois imprima os
# resultados cadastrados utilizando uma estrutura de
# repetição for.

import os


os.system('cls')

print('-' * 70)
print('Seja bem-vindo ao programa!')
print('Vamos fazer o cadastro de alunos no sistema, e mostrá-los.')
print('=' * 70)

def cadastrar_aluno(nome, matricula, nascimento):
    aluno_cadastrado = dict()
    aluno_cadastrado['Nome'] = nome
    aluno_cadastrado['Matrícula'] = matricula
    aluno_cadastrado['Nascimento'] = nascimento
    
    for key, value in aluno_cadastrado:
        print(f'{key}: {value}')
        
aluno_cadastrado = dict(nome = 'Coly', matricula = '817147', nascimento = '15/03/2000')

cadastrar_aluno(**aluno_cadastrado)

print('-' * 70)
print('Fim do programa')
print()