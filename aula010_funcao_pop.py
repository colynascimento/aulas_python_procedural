# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Colyana Magalhães da Silva Nascimento
# Data: 10/06/2024
# Aula 010 - Estruturas de Dados: Métodos e Funções - Pop

import os


os.system('cls')

# Inicializa uma lista de exemplo
lista_numeros = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# Solicita ao usuário para inserir um índice para remover o elemento
indice = int(input('Digite o índice do elemento a ser removido [0-9]: '))

# Verifica se o índice está dentro do intervalo válido da lista
if 0 <= indice < len(lista_numeros):
    # Remove o elemento no índice especificado e exibe-o
    elemento_removido = lista_numeros.pop(indice)
    print(f'Elemento removido = {elemento_removido}')
else:
    print('Índice invalido!')

# Exibe a lista resultante
print(f'Lista após remoção: {lista_numeros}')
