# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Colyana Magalhães da Silva Nascimento
# Data: 14/05/2024
# Aula 006 - Funções Internas: Biblioteca Random

# Importando as bibliotecas
import os
import random


os.system('cls')

print('-' * 70)
print('BIBLIOTECA RANDOM')
print('-' * 70)

print('Número aleatório')
numero_aleatorio = random.random()
print(f'O número gerado foi: {numero_aleatorio}')
print('.' * 70)

print('Número aleatório inteiro')
aleatorio_inteiro = random.randint(1, 20)
print(f'O número aleatório inteiro gerado foi: {aleatorio_inteiro}')
print('.' * 70)

print('Número aleatório decimal no intervalo')
aleatorio_decimal = random.uniform(1, 10)
print(f'O número decimal gerado foi: {aleatorio_decimal}')
print('.' * 70)

print('Sorteio em uma lista')
lista = ['Ágata', 'Coly', 'Isis', 'Bia']
nome_sorteado = random.choice(lista)
print(f'Lista: {lista}')
print(f'O nome escolhido foi: {nome_sorteado}')
print('.' * 70)

print('Embaralhar sequência')
lista2 = ['Ágata', 'Coly', 'Isis', 'Bia']
print(f'Lista antiga: {lista2}')
# Embaralhado = list(random.suffle(lista)) dá erro
# Embaralhado = random.suffle(lista) saída vazia
random.shuffle(lista2)
print(f'Lista nova: {lista2}')
print('.' * 70)

print('Retorno de elementos únicos de uma população')
numeros = [1, 2, 3, 4, 5, 6, 7]
amostra_aleatoria = random.sample(numeros, 5)
print(f'Retorno de amostragem: {amostra_aleatoria}')
print('.' * 70)