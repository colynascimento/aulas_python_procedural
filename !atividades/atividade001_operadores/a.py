# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Colyana Magalhães da Silva Nascimento
# Data: 18/04/2024
# Atividade 001 - Operadores aritméticos

# a. Faça um programa que peça 3 valores, depois calcule e imprima a soma e a multiplicação desses valores.

import os


os.system('cls')


# Entrada
valor1 = float(input('Digite o 1º valor: '))
valor2 = float(input('Digite o 2º valor: '))
valor3 = float(input('Digite o 3º valor: '))

# Processamento
soma_dos_valores = valor1 + valor2 + valor3
multiplicacao_dos_valores = valor1 * valor2 * valor3

#Saída
print(f'A soma de {valor1} + {valor2} + {valor3} é {soma_dos_valores}')
print(f'Já a multiplicação de {valor1} × {valor2} × {valor3} é {multiplicacao_dos_valores}')