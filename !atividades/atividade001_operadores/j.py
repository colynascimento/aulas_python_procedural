# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Colyana Magalhães da Silva Nascimento
# Data: 18/04/2024
# Atividade 001 - Operadores aritméticos

# j. Faça um programa com entrada de dados para calcular o perímetro de um retângulo.

import os


os.system('cls')

# Entrada
comprimento = float(input('Digite o valor do comprimento do retângulo: '))
largura = float(input('Digite o valor da largura do retângulo: '))

# Processamento
perimetro = (comprimento * 2) + (largura * 2)

# Saída
print(f'O perímetro do retângulo é: {perimetro}')