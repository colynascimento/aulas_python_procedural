# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Colyana Magalhães da Silva Nascimento
# Data: 17/06/2024
# Atividade 006: Listas

# D) Faça um programa que preencha uma lista com as notas de 4
# alunos, depois imprima a média.

import os


os.system

print('-' * 70)
print('Seja bem-vindo ao programa!')
print('Vamos analisar a nota de 4 alunos:')
print('=' * 70)

soma = 0

for i in range(1, 5):
    nota = float(input(f'Insira a nota do {i}º aluno: '))
    soma += nota
    
media = soma / 4

print('')
print(f'A média da nota dos alunos é: {media}')

print('-' * 70)
print('Fim do programa')
print('')