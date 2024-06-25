# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Colyana Magalhães da Silva Nascimento
# Data: 24/06/2024
# Aula 011 - Estruturas de Dados: Métodos - Tuplas

import os


os.system('cls')

# Solicitar ao usuário a quantidade de elementos na tupla
numero_elementos = int(input('Quantos elementos tem na tupla? '))

# Inicializar uma lista vazia para armazenar os elementos
elementos = []

# Estrutura de repetição para obter os elementos do usuário
for i in range(numero_elementos):
    while True:
        valor = input(f'Digite o valor {i + 1}: ')
        if valor.isdigit():
            elementos.append(int(valor))
            break
        else:
            print('Entrada inválida. Digite um número.')
            
# Converter a lista para uma tupla
tupla = tuple(elementos)

print('-' * 70)
# Exibir na tela a tupla criada
print(f'Tupla criada: {tupla}')
print('-' * 70)

# Estrutura de repetição para permitir múltiplas operações até que o
# usuário deseje sair
while True:
    # Condicional para verificar a preesença de um número específico
    valor = int(input('Verificar se o número está na Tupla: '))
    
    if valor in tupla:
        print(f'O número {valor} está na tupla.')
        # Contar o número de vezes que o número aparece
        contagem = tupla.count(valor)
        print(f'O número {valor} aparece {contagem} vez(es).')
        # Encontrar o índice da primeira ocorrência
        
        indice = tupla.index(valor)
        print(f'A 1ª ocorrência de {valor} está no índice {indice}.')
        
    else:
        print(f'O número {valor} não está na tupla.')
        
    # Perguntar ao usuário se deseja realizar outra operação ou sair
    continuar = input('Deseja continuar? (s/n): ').lower()
    if continuar != 's':
        print('Encerrando o programa. Até mais!')
    
        print('-' * 70)
        print('Fim do programa!')
        print('-' * 70)
        print()
        
        break