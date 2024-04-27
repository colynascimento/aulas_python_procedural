# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Colyana Magalhães da Silva Nascimento
# Data: 26/04/2024
# Atividade 002: Condicionais

# D) A empresa "SalaryBoost" está implementando um sistema automatizado para 
# calcular os aumentos salariais de seus funcionários com base em critérios 
# específicos. Eles precisam de um programa que receba como entrada o salário atual
# de um funcionário e, em seguida, calcule o novo salário com base em determinadas 
# condições. Essas condições incluem um aumento de 5% caso o salário atual seja 
# superior a R$1500,00, e um aumento de 10% caso o salário atual seja inferior a 
# R$1000,00. Além disso, o programa deve garantir que o salário informado não seja 
# igual a zero ou negativo, pois isso não seria válido.

import os


os.system('cls')

# Variável
salario = float(input('Insira o salário atual do funcionário: '))

# Condicionais
if salario > 1500:
    salario = salario * 1.05
    print(f'O novo salário será de R${salario:.2f}')
elif salario < 1000:
    salario = salario * 1.10
    print(f'O novo salário será de R${salario:.2f}')
elif salario <= 0:
    print('O salário informado é inválido.')
else:
    print('Não houve aumento de salário.')