# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Colyana Magalhães da Silva Nascimento
# Data: 11/06/2024
# Aula 010 - Estruturas de Dados: Métodos e Funções - Reverse

import os


os.system('cls')

print('-' * 70)
print('ESTRUTURA DE DADOS: FUNÇÃO .REVERSE()')
print('=' * 70)

# Solicita ao usuário para inserir números separados por espaço
entrada = input('Digite números separados por espaço: ')

# Divide a string de entrada em uma lista de strings
numeros_str = entrada.split()

# Converte a lista de strings em uma lista de inteiros
numeros = []
for num_str in numeros_str:
    numeros.append(int(num_str))

# Exibe a lista fornecida para referência
print(f'Lista fornecida: {numeros}')

# Solicita ao usuário pra decidir se deseja inverter a ordem
escolha = input('Deseja inverter a ordem da lista? (s/n) ').strip().lower()

# Verifica a esclha do usuário e inverte a lista se a resposta for 's'
if escolha == 's':
    numeros.reverse()
    print(f'Lista invertida: {numeros}')
else:
    print('A lista não foi invertida')
    
print('-' * 70)
print('Fim do programa!')
print('-' * 70)