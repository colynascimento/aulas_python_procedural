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


os.system('cls')

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
    print(f'Qual é a capital do estado {estado_randomico}?')


