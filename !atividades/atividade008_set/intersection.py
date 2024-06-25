# Trabalho sobre a estrutura de dados SET
# Senac Minas Gerais/Juiz de Fora
# Aluna: Colyana Magalhães da Silva Nascimento
# Turma 0152
# Data: 24/06/2024

# Estrutura de Dados: Método Intersection/&

import os


os.system('cls')

print('-' * 70)
print('Estrutura de dados: SET - Método Intersection')
print('=' * 70)

# Primeiro vamos definir dois sets
numeros1 = {0, 1, 2, 3, 4, 5}
numeros2 = {4, 5, 6, 7, 8, 9}

# Usando o método intersection
intersecao_numeros = numeros1.intersection(numeros2)

print()
print('Interseção de Dois Conjuntos')
print(f'Conjunto 1: {numeros1}')
print(f'Conjunto 2: {numeros2}')
print(f'Interseção: {intersecao_numeros}')

# Agora vamos definir três sets
letras1 = {'a', 'e', 'i', 'o', 'u'}
letras2 = {'a', 'b', 'c', 'd', 'e'}
letras3 = {'e', 'f', 'g', 'h', 'i'}

# E usar o método intersection novamente, dessa vez incluindo 
# mais de uma variável como argumento
intersecao_letras = letras1.intersection(letras2, letras3)

# Perceba como ao printar os conjuntos no terminal, a ordem de
# cada conjunto é modificada. 
# É uma característica do set que não interfere no resultado.
print()
print('Interseção de Três Conjuntos')
print(f'Conjunto 1: {letras1}')
print(f'Conjunto 2: {letras2}')
print(f'Conjunto 3: {letras3}')
print(f'Interseção: {intersecao_letras}')

# Usando os mesmos conjuntos, vamos demonstrar como a mesma operação
# pode ser feita usando o símbolo '&'
intersecao_letras2 = letras1 & letras2 & letras3

print()
print('Interseção de Três Conjuntos')
print(f'Conjunto 1: {letras1}')
print(f'Conjunto 2: {letras2}')
print(f'Conjunto 3: {letras3}')
print(f'Interseção: {intersecao_letras2}')