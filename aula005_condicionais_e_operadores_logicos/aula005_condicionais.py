# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Colyana Magalhães da Silva Nascimento
# Data: 24/04/2024
# Aula 005 - Estudo de Condicional: Parte 1

import os

os.system('cls')

print('-' * 70)
print('Estudo de Condicional: Parte 1')
print('=' * 70)

# Entrada
valor = float(input('Digite um número decimal: '))
resposta = ''

# Condicional
if valor % 1 == 0:
    valor = int(valor)
    resposta = f'Entrada incorreta, o valor {valor} é um inteiro'
else:
    resposta = f'Entrada correta, o valor {valor} é um decimal!'

# Saída
print('-' * 70)
print(resposta)

print('Fim do programa!\n')