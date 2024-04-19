# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Colyana Magalhães da Silva Nascimento
# Data: 18/04/2024
# Atividade 001 - Operadores aritméticos

# b. Faça um programa que peça o ano do seu nascimento e calcule a sua idade.

import os

import datetime

os.system('cls')

# Entrada
ano_nascimento = int(input('Digite o ano do seu nascimento: '))
ano_atual = datetime.datetime.now().year

# Processamento
idade_com_aniversario = ano_atual - ano_nascimento
idade_sem_aniversario = idade_com_aniversario - 1

# Saída
print(f'Se você já fez aniversário esse ano, sua idade é {idade_com_aniversario}. '
      f'Caso contrário, você tem {idade_sem_aniversario} anos.')
