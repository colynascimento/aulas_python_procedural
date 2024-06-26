# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Colyana Magalhães da Silva Nascimento
# Data: 10/06/2024
# Aula 010 - Estruturas de Dados: Funções e Métodos - Insert

import os


os.system('cls')

print('-' * 70)
print('ESTRUTURAS DE DADOS: .INSERT()')
print('=' * 70)

# Lista original
lista = [1, 2, 3, 4]

# Pedindo o usuário para fornecer a posição e o elemento a ser inserido
posicao = int(input('Posição onde deseja inserir o elemento: '))
elemento = input('Elemento a ser inserido: ')

# Verificando se a posição fornecida pelo usuário é válida
if posicao >= 0 and posicao <= len(lista):
    # Inserindo o elemento na lista na posição indicada pelo usuário
    lista.insert(posicao, elemento)
    print(f'Lista após inserção: {lista}')
else:
    print(f'Posição fora do intervalo entre 0 e {len(lista)}')