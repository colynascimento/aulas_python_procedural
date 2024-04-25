# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Colyana Magalhães da Silva Nascimento
# Data: 25/04/2024
# Aula 005 - Estudo de Condicional: Parte 4
# Operadores Lógicos

import os

os.system('cls')


# Declaração
a = 10
b = 5
c = 'José'

print('-' * 70)
print('Condicionias: Operadores Lógicos')
print('=' * 70)

# Condicionais e Saída
# E (and) VERDADEIRO
print('E (and) VERDADEIRO')
if (a > 5 and b != c ):
    print('Verdadeiro: Bloco executado')
else:
    print('Falso: Bloco não executado')
    
print('.' * 70)

# E (and) FALSO
print('E (and) FALSO')
if (a > 5 and b == c):
    print('Verdadeiro: Bloco executado')
else:
    print('Falso: Bloco não executado')

print('.' * 70)

# OU (or) VERDADEIRO
print('OU (or) VERDADEIRO')
if (a > 5 or b == c):
    print('Verdadeiro: Bloco executado')
else:
    print('Falso: Bloco não executado')
    
print('.' * 70)

# OU (or) FALSO
print('OU (or) FALSO')
if (a < 5 or b == 'Jane'):
    print('Verdadeiro: Bloco executado')
else:
    print('Falso: Bloco não executado')
print('-' * 70)
print()