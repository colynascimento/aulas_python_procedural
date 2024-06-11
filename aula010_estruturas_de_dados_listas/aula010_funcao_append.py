# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Colyana Magalhães da Silva Nascimento
# Data: 10/06/2024
# Aula 010 - Estruturas de Dados: Métodos e Funções - Append

import os


os.system('cls')

print('-' * 70)
print('ESTRUTURA DE DADOS; FUNÇÃO .APPEND()')
print('=' * 70)

# Inicializa uma lista vazia
lista_numeros = []

# Pede ao usuário para inserir três números
for i in range(3):
    numero = int(input('Digite um número: '))

    # Adiciona o número a lista
    lista_numeros.append(numero)

# Verifica se o número inserido está na lista e exibe uma mensagem correspondente

numero_verificar = int(input('Verifique o número: '))

if numero_verificar in lista_numeros:
    print(f'O número {numero_verificar} está na lista!')
else:
    print(f'O número {numero_verificar} não está na lista.')
