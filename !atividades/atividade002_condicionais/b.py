# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Colyana Magalhães da Silva Nascimento
# Data: 25/04/2024
# Atividade 002: Condicionais

# B) A empresa "DataMax" está desenvolvendo um novo software de análise estatística
# e precisa de uma funcionalidade que permita aos usuários inserir três números e, 
# em seguida, exibir na tela qual é o maior número, qual é o menor número ou se os 
# números são todos iguais. Essa funcionalidade é crucial para os analistas de dados 
# da "DataMax" que trabalham com conjuntos de dados diversos e precisam rapidamente 
# identificar as características básicas desses conjuntos, como a presença de outliers 
# ou a uniformidade dos números.

import os


os.system('cls')

# Entrada
numero_1 = float(input('Digite um número: '))
numero_2 = float(input('Digite mais um número: '))
numero_3 = float(input('Digite um número outra vez: '))
maior = float()
menor = float()

# Processamento
# Encontrando o maior número
if (numero_1 > numero_2 and numero_1 > numero_3):
    maior = numero_1
elif (numero_2 > numero_1 and numero_2 > numero_3):
    maior = numero_2
elif (numero_3 > numero_1 and numero_3 > numero_2):
    maior = numero_3
else:
    maior = menor

# Encontrando o menor número
if (numero_1 < numero_2 and numero_1 < numero_3):
    menor = numero_1
elif (numero_2 < numero_1 and numero_2 < numero_3):
    menor = numero_2
elif (numero_3 < numero_1 and numero_3 < numero_2):
    menor = numero_3
else:
    menor = maior
  
# Saída
if maior == menor:
    print('Os números são todos iguais.')
else:
    print(f'O maior número é: {maior}\n'
    f'O menor número é: {menor}')