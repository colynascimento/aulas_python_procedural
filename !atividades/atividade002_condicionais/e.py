# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Colyana Magalhães da Silva Nascimento
# Data: 26/04/2024
# Atividade 002: Condicionais

# E) A empresa "TravelCalc" está desenvolvendo um sistema de cálculo de preços de
# passagens de ônibus com base na distância da viagem. Eles precisam de um programa
# que solicite ao usuário a distância a desejada e, em seguida, calcule o preço da
# passagem de acordo com as políticas da empresa. Segundo essas políticas, viagens
# de até 200 km têm um custo de R$0,70 por km rodado, enquanto viagens acima dessa
# distância passam a custar R$0,40 por km rodado.

import os


os.system('cls')

# Entrada
distancia = float(input('Insira a distancia desejada em km: '))
preco = float()

# Processamento
if distancia <= 200:
    preco = distancia * 0.70
else:
    preco = distancia * 0.40
    
# Saída
print(f'O preço estimado da viagem é de R${preco:.2f}')