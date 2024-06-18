# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Colyana Magalhães da Silva Nascimento
# Data: 17/06/2024
# Atividade 007: Listas

# A) Faça um programa que leia um número indeterminado de notas
# (pressione ‘s’ ou ‘0’ para sair). Após esta entrada de dados,
# faça o seguinte:

# • Mostre a quantidade de notas que foram lidas.
# • Exiba todas as notas na ordem em que foram informadas.
# • Exiba todas as notas na ordem inversa à que foram informadas, uma abaixo da outra.
# • Calcule e mostre a soma das notas.
# • Calcule e mostre a média das notas.

import os


os.system('cls')

print('-' * 70)
print('Seja bem-vindo ao programa!')
print('Vams analisar as notas dos alunos.')
print('=' * 70)

sair = ''
i = 1

while sair != 's':
    
    nota = input(f'Insira a {i}º nota [ou digite "s" para encerrar]: ')
    
    if nota == 's':
        sair == 's'
    
    
    i += 1
    