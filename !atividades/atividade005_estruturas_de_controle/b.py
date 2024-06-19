# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Colyana Magalhães da Silva Nascimento
# Data: 28/05/2024
# Atividade 005: Estruturas de Controle

# B) Evolua o programa anterior para um código que pergunte ao 
# usuário qual o intervalo que ele deseja ver  impresso.

import os


os.system('cls')

inicio = int(input('Insira o número inicial: '))
fim = int(input('Insira o número final: ')) + 1

for i in range(inicio, fim):
    print(f'{i}', end=' ')