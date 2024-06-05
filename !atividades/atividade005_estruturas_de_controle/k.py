# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Colyana Magalhães da Silva Nascimento
# Data: 05/06/2024
# Atividade 005: Estruturas de Controle

# k) Crie um programa que pede que o usuário digite um nome ou uma
# frase, verifique se esse conteúdo digitado é um palíndromo ou não,
# exibindo em tela esse resultado.

import os


os.system('cls')

entrada = input('Digite uma palavra ou frase: ').lower().replace(' ', '')

if entrada == entrada[::-1]:
    print('O conteúdo digitado é um palíndromo! Uau :O')
else:
    print('O conteúdo digitado não é um palíndromo.')
