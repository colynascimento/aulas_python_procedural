# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Colyana Magalhães da Silva Nascimento
# Data: 11/06/2024
# Aula 010 - Estruturas de Dados: Métodos e Funções - Count

import os


os.system('cls')

print('-' * 70)
print('ESTRUTURA DE DADOS: FUNÇÃO .COUNT()')
print('=' * 70)

# Solicita ao usuário para inserir números separados por espaço

entrada = input('Digite números separados por espaço: ')

# Divide a string de entrada em uma lista de strings
numeros_str = entrada.split()

# Converte a lista de strings em uma lista de inteiros
numeros = []
for num_str in numeros_str:
    numeros.append(int(num_str))
    
# Solicita ao usuário para inserir o número que deseja contar na lista
numero_para_contar = int(input('Digite o número que deseja contar: '))

contagem = numeros.count(numero_para_contar)

if contagem > 0:
    print(f'O número {numero_para_contar} aparece {contagem} vezes na lista.')
else:
    print(f'O número {numero_para_contar} não aparece na lista.')
    
# Exibe a lista fornecida para referência
print(f'Lista fornecida: {numeros}')

print('-' * 70)
print('Fim do programa')
print('')