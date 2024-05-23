# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Colyana Magalhães da Silva Nascimento
# Data: 21/05/2024
# Atividade 004: Strings

# Faça um programa que receba o nome 'João Silva' e, em seguida,
# substitua 'Silva' por 'Oliveira'.

import os


os.system('cls')

# Saudação
print('-' * 70)
print('Seja bem-vindo ao meu programa! Qual é o seu nome?')
print('=' * 70)

# Entrada de dados
nome = input('Digite o seu nome: ')

# Validação
caracteres_especiais = {'@', '*', '&'} # Criei um set() para alguns caracteres especiais
contem_caracteres_especiais = not caracteres_especiais.isdisjoint(nome)

# Posso também separar todas as letras em uma lista e verificar com in se o caractere especial está contido na string?

# Processamento
nome = nome.replace('Silva', 'Oliveira')

# Saída
if contem_caracteres_especiais == True:
    print('Os caracteres especiais são inválidos no campo acima.')
else:
    print(f'Olá, {nome}\n')
    
print('-' * 70)