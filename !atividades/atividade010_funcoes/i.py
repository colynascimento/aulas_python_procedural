# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Colyana Magalhães da Silva Nascimento
# Data: 11/07/2024
# Atividade 010: Funções

# I) Faça um programa de perguntas e respostas sobre os estados e
# capitais brasileiras. O programa deverá exibir para o usuário o
# estado e perguntar qual a sua capital. Se o usuário errar a resposta,
# o programa será finalizado apresentando quantas perguntas estão
# corretas. Utilize ao menos uma função e não há a necessidade de
# modularizar o código.

import os
import random
import time


os.system('cls')

contador = 0
opcao = 1

dicionario_capitais = {'Acre': 'Rio Branco', 'Alagoas': 'Maceió', 'Amapá': 'Macapá', 'Amazonas': 'Manaus', 'Bahia': 'Salvador',
                      'Ceará': 'Fortaleza', 'Distrito Federal': 'Brasília', 'Espírito Santo': 'Vitória', 'Goiás': 'Goiânia',
                      'Maranhão': 'São Luís', 'Mato Grosso': 'Cuiabá', 'Mato Grosso do Sul': 'Campo Grande', 'Minas Gerais': 'Belo Horizonte',
                      'Pará': 'Belém', 'Paraíba': 'João Pessoa', 'Paraná': 'Curitiba', 'Pernambuco': 'Recife', 'Piauí': 'Teresina',
                      'Rio de Janeiro': 'Rio de Janeiro', 'Rio Grande do Norte': 'Natal', 'Rio Grande do Sul': 'Porto Alegre',
                      'Rondônia': 'Porto Velho', 'Roraima': 'Boa Vista', 'Santa Catarina': 'Florianópolis', 'São Paulo': 'São Paulo',
                      'Sergipe': 'Aracaju', 'Tocantins': 'Palmas'}

def definir_estado():
    estado = list(dicionario_capitais.keys())
    estado_randomico = random.choice(estado)
    return estado_randomico


def verificar_resposta(estado, resposta):
    if estado in dicionario_capitais:
        return dicionario_capitais[estado] == resposta
    else:
        return False


def capital_correta(estado):
    if estado in dicionario_capitais:
        return dicionario_capitais[estado]


def menu_opcoes():
    print('+------------------------------------------------+')
    print('|               Deseja continuar?                |')
    print('|           1 - Sim, manda mais uma!             |')
    print('|       2 - Não, quero sair do programa          |')
    opcao = input('Sua resposta: ')
    if opcao == '1' or opcao == '2':
        return int(opcao)
    else:
        return None

while opcao == 1:
    print('+------------------------------------------------+')
    print('|                 Quiz do Brasil                 |')
    print('+------------------------------------------------+')
    print('|  Hoje vamos ver se você conhece mesmo o Brasil |')
    print('|                 Está pronto?                   |')
    input('|        Pressione Enter para começar            |')
    print('+------------------------------------------------+')
    estado_quiz = definir_estado()
    resposta_quiz = input(f'|   Qual é a capital do {estado_quiz}? ').capitalize()
    if verificar_resposta(estado_quiz, resposta_quiz):
        contador += 1
        print('|          Muito bem! Resposta correta :)        |')
        opcao = menu_opcoes()
        if opcao != 1:
            break
        else:
            print('Opção inválida! Digite apenas 1 ou 2.')
    else:
        print('|                Resposta errada!                   |')
        print(f'| A capital de {estado_quiz} é {capital_correta(estado_quiz)}.')
        print(f'|     Total de respostas corretas: {contador}              |')
        print('+------------------------------------------------+')
        opcao = '2'

print('Encerrando...')
time.sleep(1)
print('Fim do programa!')
print('-' * 50)




