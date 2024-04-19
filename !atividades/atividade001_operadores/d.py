# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Colyana Magalhães da Silva Nascimento
# Data: 18/04/2024
# Atividade 001 - Operadores aritméticos

# d. Faça um programa que receba e divida 2 números. A saída da divisão precisará ser formatada com 4 casas decimais.

import os

os.system('cls')

# Entrada
dividendo = float(input('Digite o divindendo: '))
divisor = float(input('Digite o divisor: '))

# Processamento
divisao = dividendo / divisor

# Saída
print(f'O resultado da divisão de {dividendo} ÷ {divisor} '
      f'é {divisao:.4f}')