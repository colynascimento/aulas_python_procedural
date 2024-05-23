# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Colyana Magalhães da Silva Nascimento
# Data: 21/05/2024
# Atividade 004: Strings

# G) Faça um programa que receba um número inteiro e mostre na tela:
# • A quantidade de unidades, a quantidade de dezenas, a quantidade
# de centenas e a quantidade de milhares.

# Dica: usar divisão

import os


os.system('cls')

print('-' * 70)
print('Seja bem-vindo ao programa!')
print('Vamos analisar um número qualquer.')
print('=' * 70)

# Entrada de dados
numero = int(input('Insira um número inteiro: '))

# Processamento
milhares = numero // 1000
centenas = (numero - milhares * 1000) // 100 
dezenas = (numero - (centenas * 100 + milhares * 1000)) // 10
unidades = (numero - (dezenas * 10 + centenas * 100 + milhares * 1000)) // 1

# Saída de dados
print('O número inserido tem: \n'
      f'- {milhares} milhares\n'
      f'- {centenas} centenas\n'
      f'- {dezenas} dezenas\n'
      f'- {unidades} unidades\n')

print('-' * 70)