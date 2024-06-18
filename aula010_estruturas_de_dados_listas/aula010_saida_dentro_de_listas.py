# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Colyana Magalhães da Silva Nascimento
# Data: 18/06/2024
# Aula 010 - Estruturas de Dados: Métodos e Funções - Saída de Listas Dentro de Listas

import os


os.system('cls')

print('-' * 70)
print('ESTRUTURAS DE CONTROLE: Varrendo Listas Dentro de Listas')
print('=' * 70)

# Similar a um array de 3 dimensões
jogo_velha = [
    # 0    1    2
    ['X', 'O', 'X'],  # 0
    ['X', 'X', 'O'],  # 1
    ['O', 'O', 'O']  # 2
]

print(jogo_velha)
print()

# Pegando manualmente os valores
print(f'Na linha 1 coluna 1, existe um: {jogo_velha[1][1]}')
print(f'Na linha 0 coluna 2, existe um: {jogo_velha[0][2]}')

print()

# Varrendo com for range
for linha in range(0, len(jogo_velha)):
    for coluna in range(0, len(jogo_velha)):
        print(jogo_velha[linha][coluna], end=' ')
    print()

print()
print('-' * 70)
print('Fim do programa')
print()
