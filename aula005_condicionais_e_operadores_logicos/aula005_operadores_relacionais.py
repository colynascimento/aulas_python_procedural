# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Colyana Magalhães da Silva Nascimento
# Data: 25/04/2024
# Aula 005 - Estudo de Condicional: Parte 3
# Operadores Relacionais

import os

os.system('cls')


# Declarações
a = 10
b = 5
c = 'José'
d = 'José'

print('-' * 70)
print('Condicionais: Operadores Relacionais')
print('=' * 70)

# Condicionais
# Igualdade (==)
if c == d:
    print(f'{c} é igual a {d}')
else:
    print(f'{c} não é igual a {d}')
    
# Diferença (!=)
if a != c:
    print('-' * 70)
    print(f'{a} é diferente de {c}')
else:
    print(f'{a} não é diferente de {c}')
    
# Maior que (>)
if a > b:
    print('-' * 70)
    print(f'{a} é maior que {b}')
else:
    print(f'{a} não é maior que {b}')
    
# Menor que (<)
if b < a:
    print('-' * 70)
    print(f'{b} é menor que {a}')
else:
    print(f'{b} não é menor que {a}')
    
# Maior ou igual a (>=)
if a >= b:
    print('-' * 70)
    print(f'{a} é maior ou igual a {b}')
else:
    print(f'{a} não é maior ou igual a {b}')
    
# Menor ou igual a (<=)
if b <= a:
    print('-' * 70)
    print(f'{b} é menor ou igual a {a}')
    print('=' * 70)
else:
    print(f'{b} não é menor ou igual a {a}')
    
print('Fim do programa!')
print('-' * 70)
