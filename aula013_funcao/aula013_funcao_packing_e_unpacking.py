# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Colyana Magalhães da Silva Nascimento
# Data: 11/07/2024
# Aula 013 - Funções: Retorno

import os


os.system('cls')

# Definindo uma função para empacotar
def empacotar(*lista_numeros):
    print(f'Empacotados: {lista_numeros}')
    for i in lista_numeros:
        print(f'Empacotado: {i}')
        
# Invocando a função empacotar
empacotar(1, 2, 3, 4, 5)

# Desempacotando (Lista)
def desempacotar(a, b, c, d, e):
    print('Desempacotar:')
    print(f'a = {a}')
    print(f'b = {b}')
    print(f'c = {c}')
    print(f'd = {d}')
    print(f'e = {e}')
    
# Invocando a função desempacotar
lista_numeros = [1, 2, 3, 4, 5] # Lista
desempacotar(*lista_numeros) # * Args

# Packing dicionário
def empacotar_dicionario(**dados_dicionario): # **Kwargs
    print(f'Dados do dicionário: {dados_dicionario}')
    for key, value in dados_dicionario.items():
        print(f'Chave: {key}, Valor: {value}') 
        
print('-' * 70)
print('--Dicionário')
empacotar_dicionario(nome = 'Juquinha', idade = 70, peso = 70.5)

# Unpacking dicionário
print('-' * 70)
def desempacotar_dicionario(nome, idade, peso):
    print(f'Nome = {nome}')
    print(f'Idade = {idade}')
    print(f'Peso = {peso}')
    
dicionario = dict(nome = 'Maria', idade = 70, peso = 70.5)
desempacotar_dicionario(**dicionario)
print()