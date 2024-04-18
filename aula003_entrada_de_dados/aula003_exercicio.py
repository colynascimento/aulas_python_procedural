# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Colyana Magalhães da Silva Nascimento
# Data: 17/04/2024
# Exercício: Variáveis, casting e template string

import os


os.system('cls')

print('-' * 70)
print('EXERCÍCIO DE VARIÁVEIS, CASTING E TEMPLATE STRING')
print('=' * 70)

# Entrada
nome = str(input('Digite seu nome: '))
numero = int(input('Digite um número inteiro de 1 a 10: '))
recorde = float(input('Digite um número de 0 a 1: '))
boolean = False

# Saída interpolada
print('-' * 70)
print('SAÍDA DE DADOS')
print('=' * 70)
print(f'Parabéns {nome}! Verificador de surtos = {boolean}. Estamos trabalhando a {numero} dias sem surtos!') 
print('Seu recorde é {recorde} dia até o momento.')
print('A variável nome é do tipo: ', type(nome))
print('A variável numero é do tipo: ', type(numero))
print('A variável recorde é do tipo: ', type(recorde))
print('A variável boolean é do tipo: ', type(boolean))