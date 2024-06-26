# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Colyana Magalhães da Silva Nascimento
# Data: 11/06/2024
# Aula 010 - Estruturas de Dados: Métodos e Funções - Clear

import os


os.system('cls')

print('-' * 70)
print('ESTRUTURA DE DADOS: FUNÇÃO .CLEAR()')
print('=' * 70)

# Solicita ao usuário para inserir números separados por espaço
entrada = input('Digite números separados por espaço: ')

# Divide a string de entrada em uma lista de strings
numeros_str = entrada.split()

# Converte a lista de strings em uma lista de inteiros
numeros = []
for num_str in numeros_str:
    numeros.append(int(num_str))
    
# Solicita ao usuário para decidir se deseja limpar a lista
escolha = input('Deseja limpar a lista? (s/n): ').strip().lower()

# Verifica a escolha do usuário e limpa a lista se a resposta for 's'
if escolha == 's':
    numeros.clear()
    print(f'Lista limpa: {numeros}')
else:
    print('A lista não foi limpa.')

# Exibe a lista fornecida para referência
print(f'Lista fornecida: {numeros}')

print('-' * 70)
print('Fim do programa!')
print('-' * 70)