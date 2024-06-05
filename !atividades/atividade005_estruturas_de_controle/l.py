# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Colyana Magalhães da Silva Nascimento
# Data: 05/06/2024
# Atividade 005: Estruturas de Controle

# l) Faça um programa que verifique se o usuário e senha estão
# inseridos em um banco de dados (fake). O usuário só terá acesso se
# digitar os dados corretos e, assim, sair do laço.

import os


os.system('cls')

dados_usuario = ['Agata', 'Arthur', 'Augusto', 'Bia', 'Brendon', 'Bruno',
                 'Coly', 'Danilo', 'Dian', 'Giu', 'Isis', 'Leo', 'Moises', 'Vini']
dados_senha = '14789632'

usuario = input('Usuário: ')
senha = input('Senha: ')

if usuario not in dados_usuario:
    print('Usuário não encontrado')
elif dados_senha == senha:
    print('Login efetuado com sucesso!')
else:
    print('Senha incorreta')
