# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Colyana Magalhães da Silva Nascimento
# Data: 14/05/2024
# Atividade 003: Funções/Métodos Internos

# D) Faça um programa que receba um ângulo qualquer. Em seguida,
# calcule o seno, cosseno e tangente do ângulo, limitando a saída a 2
# casas decimais.

import os
import math


os.system('cls')

print('-' * 70)
print('ATIVIDADE 3: Questão D')
print('Triângulo')
print('=' * 70)

# Recebendo o valor do ângulo
angulo = float(input('Insira o valor do ângulo: '))

# Processamento
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

# Saída
# Validação divisão por zero
if cosseno == 0:
    print('O cosseno não pode ser zero.')
else:
    print(f'O seno do triângulo é {seno:.2f}º\n'
        f'O cosseno do triângulo é {cosseno:.2f}º\n'
        f'A tangente do triângulo é {tangente:.2f}º.')

print('-' * 70)
print()