# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Colyana Magalhães da Silva Nascimento
# Data: 11/07/2024
# Atividade 010: Funções

# G) Crie um programa que peça ao usuário 2 números maiores que 0 e
# menores que 11. Depois mostre um menu com as seguintes operações:
# 1. Soma
# 2. Subtração
# 3. Produto
# 4. Divisão
# 4. Divisão inteira
# 6. Resto da divisão
# O usuário deverá escolher um número maior ou igual a 1 e menor ou
# igual a 6. Em seguida, você criará funções que retornem os
# resultados das operações, imprimindo os resultados na tela.

import os


os.system('cls')


def soma(x, y):
    return x + y


def subtracao(x, y):
    return x - y


def produto(x, y):
    return x * y


def divisao(x,y):
    return x / y


def divisao_inteira(x, y):
    return x // y


def resto_divisao(x, y):
    return x % y


print('+------------------------------------------------+')
print('|         Seja bem-vindo ao programa!            |')
print('|       Vamos fazer operações matemáticas?       |')
print('=' * 50)
numero_1 = float(input('|   Digite um número de 0 a 11: '))
numero_2 = float(input('|   Digite outro número de 0 a 11: '))
print('|            1. Soma                             |')
print('|            2. Subtração                        |')
print('|            3. Produto                          |')
print('|            4. Divisão                          |')
print('|            5. Divisão inteira                  |')
print('|            6. Resto da divisão                 |')
print('+------------------------------------------------+')

while True:
    opcao = input('\n|  Qual operação iremos fazer? (1-6): ')

    if opcao == '1':
        resultado = soma(numero_1, numero_2)
        print(f'|   {numero_1} + {numero_2} = {resultado}')
    elif opcao == '2':
        resultado = subtracao(numero_1, numero_2)
        print(f'|   {numero_1} - {numero_2} = {resultado}')
    elif opcao == '3':
        resultado = produto(numero_1, numero_2)
        print(f'|   {numero_1} * {numero_2} = {resultado}')
    elif opcao == '4':
        resultado = divisao(numero_1, numero_2)
        print(f'|   {numero_1} / {numero_2} = {resultado}')
    elif opcao == '5':
        resultado = divisao_inteira(numero_1, numero_2)
        print(f'|   {numero_1} // {numero_2} = {resultado}')
    elif opcao == '6':
        resultado = resto_divisao(numero_1, numero_2)
        print(f'|   {numero_1} % {numero_2} = {resultado}')
    else:
        print('|      Operação inválida.                        ')
        print('| Por favor digite apenas um número de 1 a 6, conforme as opções acima')
        input('| Aperte Enter para continuar...                        ')
        continue
    break

print()
print('Fim do programa!')
print('-' * 70)