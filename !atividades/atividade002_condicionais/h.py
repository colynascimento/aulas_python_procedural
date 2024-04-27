# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Colyana Magalhães da Silva Nascimento
# Data: 26/04/2024
# Atividade 002: Condicionais

# H) A empresa "RootCalc" está desenvolvendo um software de cálculo de raízes de 
# equações quadráticas para auxiliar engenheiros e cientistas em suas análises e
# projetos. Eles precisam de um programa que calcule as raízes da equação 
# quadrática 𝑥²−6𝑥+5 sem depender de funções ou métodos predefinidos, utilizando
# apenas os conceitos e operações básicas aprendidos até o momento. Essas raízes 
# são conhecidas como 𝑥’ = 5 e 𝑥’’ = 1, e o programa deve ser capaz de calcular
# essas raízes de forma precisa, seguindo os princípios matemáticos fundamentais.

import os


os.system('cls')

# Variáveis
a = 1
b = -6
c = 5
x = int()

# 1º - Achando delta
delta = b ** 2 - 4 * a * c

# 2º - Achando x'
x1 = (- b + delta ** 0.5) / 2 * a

# 3º - Achando x''
x2 = (- b - delta ** 0.5) / 2 * a

# Verificação
if x1 == 5 and x2 == 1:
    print('O programa é capaz de calcular a equação corretamente.')
else:
    print('O programa está com erro. Entre em contato com o suporte.')