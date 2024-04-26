# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Colyana Magalhães da Silva Nascimento
# Data: 25/04/2024
# Atividade 002: Condicionais

#A) A empresa "TechSolutions" contratou você para desenvolver um programa em Python 
# que irá automatizar uma parte do seu sistema de processamento de dados. Eles 
# precisam de um programa que solicite ao usuário a entrada de um número inteiro e, 
# em seguida, verifique se esse número é par ou ímpar. Essa funcionalidade é essencial 
# para o sistema deles, pois eles processam grandes conjuntos de dados e precisam classificar 
# os números de forma eficiente para realizar cálculos específicos em cada tipo de número.

import os


os.system('cls')

# Entrada
numero_inteiro = int(input('Digite um número inteiro: '))
resposta = ''

# Processamento
if numero_inteiro % 2 == 0:
    resposta = f'{numero_inteiro} é um número par.'
else:
    resposta = f'{numero_inteiro} é um número ímpar.'
    
# Saída
print(resposta)
