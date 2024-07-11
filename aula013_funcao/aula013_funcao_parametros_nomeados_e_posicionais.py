# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Colyana Magalhães da Silva Nascimento
# Data: 09/07/2024
# Aula 013 - Funções: Parâmetros Posicionais e Nomeados

import os


os.system('cls')

# Definindo a função


def dados_paciente(nome='Coly', nascimento=2005, peso=46, altura=1.68):
    print(f'Bem-vindo(a) ao sistema Senac, {nome}!')
    print(f'O ano de nascimento da {nome} é {nascimento}.')
    print(f'O peso da {nome} é {peso}Kg.')
    print(f'A altura da {nome} é {altura}m.')
    print('-' * 70)


def posicional_nomeado(nascimento, nome='Coly'):  # Ok! Funciona
    print(f'Bem-vindo(a) ao sistema Senac, {nome}!')
    print(f'O ano de nascimento da {nome} é {nascimento}.')
    print('-' * 70)


def nomeado_posicional(nome='Coly', nascimento):  # Not Ok! Não funciona
    print(f'Bem-vindo(a) ao sistema Senac, {nome}!')
    print(f'O ano de nascimento da {nome} é {nascimento}.')
    print('-' * 70)


# Invocando a função
dados_paciente()

dados_paciente(nome='Isis', nascimento=1985, peso=46, altura=1.56)
dados_paciente(nascimento=2008, nome='Ágata', peso=46, altura=1.58)
dados_paciente(altura=1.66, peso=46, nome='Bia', nascimento=2008)