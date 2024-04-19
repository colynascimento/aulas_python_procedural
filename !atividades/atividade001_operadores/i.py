# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Colyana Magalhães da Silva Nascimento
# Data: 18/04/2024
# Atividade 001 - Operadores aritméticos

# i. Faça um programa que receba um valor em reais, depois calcule quantos dólares daria para comprar com esse valor.

import os


os.system('cls')

# Entrada
valor_em_real = float(input('Digite um valor em real: '))

# Processamento
valor_em_dolar = valor_em_real * 5.25

#Saída
print(f'R${valor_em_real:.2f} equivalem a US{valor_em_dolar:.2f}')
