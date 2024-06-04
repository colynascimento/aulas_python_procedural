# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Colyana Magalhães da Silva Nascimento
# Data: 28/05/2024
# Atividade 005: Estruturas de Controle

# F) Faça um programa que imprima os números primos entre 0 e 100.

import os


os.system('cls')

for numero in range(2, 100):
    primo = True
    
    for i in range(2, numero):
        if (numero % i == 0):
            primo = False
            break
    
    if primo == True:
            print(numero)