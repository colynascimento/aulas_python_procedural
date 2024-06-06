# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Colyana Magalhães da Silva Nascimento
# Data: 14/05/2024
# Atividade 003: Funções/Métodos Internos

# A) Faça um programa que receba um valor e mostre sua raiz quadrada.
# Para raízes que não são exatas, arredonde para cima ou para baixo. 
# Faça a validação para números negativos, avisando ao usuário que o 
# resultado será um número complexo.

import os
import math


os.system('cls')

print('-' * 70)
print('ATIVIDADE 3: Questão A')
print('Raiz Quadrada')
print('=' * 70)

# Recebendo o valor
valor = float(input('Digite um valor qualquer: '))

raiz_quadrada = math.sqrt(valor)
raiz_quadrada_arredondada = math.floor(raiz_quadrada)

# Fazendo a validação do valor recebido
if valor <= 0:
    print(f'{valor} é negativo, logo o resultado da raiz será um número complexo.')
elif raiz_quadrada.is_integer():
    raiz_quadrada = int(raiz_quadrada)
    print(f'A raiz quadrada de {valor} é {raiz_quadrada}.')
else:
    raiz_quadrada_arredondada = int(raiz_quadrada_arredondada)
    print(f'A raiz quadrada aproximada de {valor} é {raiz_quadrada_arredondada}.')
    
print('-' * 70)
print()