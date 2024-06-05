# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Colyana Magalhães da Silva Nascimento
# Data: 05/05/2024
# Atividade 005: Estruturas de Controle

# j) Crie um programa que realiza a contagem de 1 até 100, usando
# apenas de números ímpares, ao final do processo exiba na tela
# quantos números ímpares foram encontrados nesse intervalo, assim
# como a soma dos mesmos.

import os


os.system('cls')

soma = 0
impares = 0

for i in range(1, 101):

    if i % 2 != 0:
        soma += i
        impares += 1

print(f'Foram encontrados {impares} números ímpares no intervalo de 1 a 100.')
print(f'A soma dos números ímpares dentro desse intervalo é {soma}')
