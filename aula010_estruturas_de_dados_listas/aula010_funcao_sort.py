# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Colyana Magalhães da Silva Nascimento
# Data: 11/06/2024
# Aula 010 - Estruturas de Dados: Métodos e Funções - Sort

import os


os.system('cls')

print('-' * 70)
print('ESTRUTURA DE DADOS: FUNÇÃO .SORT()')
print('=' * 70)

# Solicita ao usuário para inserir números separados por espaço
entrada = input('Digite números separados por espaço: ') 

# Divide a string de entrada em uma lista de strings
numeros_str = entrada.split()

# Converte a lista de strings em uma lista de inteiros
numeros = []
for num_str in numeros_str:
    numeros.append(int(num_str))
    
# Solicita ao usuário para escolher a ordem de classificação
ordem = input(
    'Digite "asc" para ordem ascendente ou "dec"'
    'para ordem decrescente: ').strip().lower()
    
# Verifica a escolha do usuário e ordena a lista de acordo
if ordem == 'asc':
    numeros.sort()
    print(f'Lista ordenada em ordem crescente: {numeros}')
elif ordem == 'dec':
    numeros.sort(reverse=True)
    print(f'Lista ordenada em ordem decrescente: {numeros}')
else:
    print('Opção inválida! A lista não foi ordenada.')
    
# Exibe a lista fornecida para referência
print(f'Lista fornecida: {numeros}')

print('-' * 70)
print('Fim do programa')
print()