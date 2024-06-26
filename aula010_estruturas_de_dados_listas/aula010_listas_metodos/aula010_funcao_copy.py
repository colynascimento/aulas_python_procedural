# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Colyana Magalhães da Silva Nascimento
# Data: 11/06/2024
# Aula 010 - Estruturas de Dados: Métodos e Funções - Copy

import os


os.system('cls')

print('-' * 70)
print('ESTRUTURA DE DADOS: FUNÇÃO')
print('=' * 70)

# Solicita ao usuário para inserir números separados por espaço
entrada = input('Digite números separados por espaço: ')

# Divide a string de entrada em uma lista de strigs
numeros_str = entrada.split()

# Converte a lista de strings em uma lista de inteiros
numeros = []
for num_str in numeros_str:
    numeros.append(int(num_str))
    
# Solicita ao usuário para decidir se deseja criar uma cópia da lista
escolha = input('Deseja criar uma cópia? (s/n): ').strip().lower()

# Verifica a escolha do usuário e cria uma cópia da lista se a resposta for 's'
if escolha == 's':
    lista_copiada = numeros.copy()
    print(f'Cópia da lista: {lista_copiada}')
else:
    print('A lista não foi copiada.')
    
# acrescentar = input('Deseja acrescentar um item na lista? (s/n): ').strip().lower()

# Exibe a lista fornecida para referêcia
print(f'Lista fornecida {numeros}')

print('-' * 70)
print('Fim do programa!')
print('-' * 70)