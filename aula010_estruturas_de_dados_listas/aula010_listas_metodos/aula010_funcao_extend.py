# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Colyana Magalhães da Silva Nascimento
# Data: 10/06/2024
# Aula 010 - Estruturas de Dados: Métodos e Funções - Extend

import os


os.system('cls')

print('-' * 70)
print('ESTRUTURAS DE DADOS: FUNÇÃO .EXTEND()')
print('=' * 70)

# Inicializa uma lista vazia
lista_numeros = []

# Solicita ao usuário para inserir números separados por espaço
entrada = input('Digite números separados por espaço: ')

# Divide a string de entrada em uma lista de strings
numeros = entrada.split()

# Cria uma lista para armazenar números pares
pares = []

# Itera sobre os números inseridos
for numero in numeros:
    # Converte a string para inteiro
    numero_aux = int(numero)
    # Verifica se o número é par
    if numero_aux % 2 == 0:
        # Adiciona o número par à lista de pares
        pares.append(numero_aux)

# Usa o .extend() para adicionar todos os números pares à lista principal
lista_numeros.extend(pares)

# Exibe a lista resultante
print(f'Números pares adicionados à lista: {lista_numeros}')

print('-' * 70)
print('Fim do programa!')
print('-' * 70)