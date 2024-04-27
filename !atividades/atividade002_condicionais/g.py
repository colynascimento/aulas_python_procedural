# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Colyana Magalhães da Silva Nascimento
# Data: 26/04/2024
# Atividade 002: Condicionais

# G) Você está desenvolvendo um programa para determinar se três segmentos podem
# formar um triângulo. Para isso, o programa precisa receber as medidas dos três
# segmentos e compará-las entre si. A resposta resultante dessa comparação deve
# indicar se os segmentos fornecidos podem formar um triângulo ou não.

import os


os.system('cls')

# Entrada
a = int(input('Insira o tamanho do primeiro cateto: '))
b = int(input('Insira o tamanho do segundo cateto: '))
c = int(input('Insira o tamanho da hipotenusa: '))
triangulo = bool()

# Condicionais
if (a + b > c and b + c > a and a + c > b):
    triangulo = True
else:
    triangulo = False
    
# Saída
if triangulo == True:
    print('O triângulo é válido △ :)')
else:
    print('Os segmentos fornecidos não podem formar um triângulo :(')