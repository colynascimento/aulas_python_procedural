# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Colyana Magalhães da Silva Nascimento
# Data: 26/04/2024
# Atividade 002: Condicionais

# F) A empresa "LeapYearCheck" está desenvolvendo um software de verificação de 
# anos bissextos para auxiliar usuários na identificação desses anos de forma 
# rápida e precisa. Eles precisam de um programa que permita aos usuários inserir
# um ano e, em seguida, determine se esse ano é bissexto ou não, de acordo com 
# as regras estabelecidas pelo calendário gregoriano. Além disso, é necessário 
# realizar a validação de entrada de dados para garantir que o ano inserido pelo 
# usuário seja um valor válido, ou seja, um número inteiro positivo.

import os


os.system('cls')

# Entrada
ano = int(input('Insira um ano: '))
bissexto = bool()

# Processamento
if (ano % 4 == 0 and ano % 100 == 0 and ano % 400 != 0):
    bissexto = False
elif ano % 4 == 0:
    bissexto = True
else:
    bissexto = False
    
# Saída
if bissexto == True:
    print(f'O ano {ano} é bissexto.')
else:
    print(f'O ano {ano} não é bissexto.')