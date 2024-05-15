# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Colyana Magalhães da Silva Nascimento
# Data: 14/05/2024
# Atividade 003: Funções/Métodos Internos

# G) Faça um programa que peça os valores de a, b e c de uma equação
# do 2º grau. Calcule as raízes da equação do 2º grau seguindo a
# fórmula: Δ = b² - 4ac, x = (-b ± raiz(Δ)) / (2a).

import os
import math


os.system('cls')

print('-' * 70)
print('ATIVIDADE 3: Questão G')
print('Fórmula de Bhaskara')
print('=' * 70)

# Recebendo os valores
a = int(input('Insira o valor de a: '))
b = int(input('Insira o valor de b: '))
c = int(input('Insira o valor de c: '))

# Calculando delta
delta = b ** 2 - 4 * a * c

# Calculando x1
x1 = (-b + math.sqrt(delta)) / (2 * a)

# Calculando x2
x2 = (-b - math.sqrt(delta)) / (2 * a)

# Saída
print(f'As raízes da equação são {x1} e {x2}.')

# Teste: 
# Para a = 1, b = -3, c = 2
# x' = 2 e x" = 1
# Para a = 1, b = -4, c = 4
# x' = 2 e x" = 2