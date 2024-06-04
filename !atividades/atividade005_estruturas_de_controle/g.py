# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Colyana Magalhães da Silva Nascimento
# Data: 28/05/2024
# Atividade 005: Estruturas de Controle

# G) Faça um programa que calcule os números primos em um intervalo
# pré-determinado pelo usuário.

import os


os.system('cls')

inicio = int(input('Insira o número inicial: '))
fim = int(input('Insira o número final: '))

for numero in range(inicio, fim):
    primo = True
    
    for i in range(2, numero):
        if (numero % i == 0):
            primo = False
            break
    
    if primo == True:
            print(numero)