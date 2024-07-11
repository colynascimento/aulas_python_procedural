# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Colyana Magalhães da Silva Nascimento
# Data: 27/06/2024
# Atv

# A) Faça um programa para criar um dicionário com 4 elementos.

import os
import random


os.system('cls')

print('-' * 70)
print('Seja bem-vindo ao programa!')
print('Vamos criar uma ficha do seu personagem de RPG.')
print('=' * 70)

personagem = {}

# Atribuindo valores
print('Vamos às características do seu personagem: ')

nome = input('Insira o nome do personagem: ')

print('\nSugestões de classe: '
      '\n→ Paladino'
      '\n→ Guerreiro'
      '\n→ Ladino'
      '\n→ Bruxo'
      '\n→ Mago'
      '\n→ Bárbaro')
classe = input('Digite a classe escolhida: ')

print('\nSugestões de raça:'
      '\n→ Humanos'
      '\n→ Elfos'
      '\n→ Gnomos'
      '\n→ Minotauros'
      '\n→ Meio-demônio')
raca = input('Digite a raça escolhida: ')

print('\nSugestões de armas: '
      '\n→ Adaga'
      '\n→ Espada'
      '\n→ Marreta'
      '\n→ Flechas'
      '\n→ Lança'
      '\n→ Maça')
arma = input('Digite a arma escolhida: ')

print('\nVamos jogar o dado de 20 lados para ver qual será sua força!')
input('Pressione Enter para jogar o dado de 20 lados...')
forca = random.randint(1, 20)
print(f'Sua força será {forca}')

print('\nVamos jogar o dado de 20 lados para ver qual será sua inteligência!')
input('Pressione Enter para jogar o dado de 20 lados...')
inteligencia = random.randint(1, 20)
print(f'Sua inteligência será {inteligencia}')

# Adicionando ao dicionário
personagem['nome'] = nome
personagem['classe'] = classe
personagem['raça'] = raca
personagem['arma'] = arma
personagem['força'] = forca
personagem['inteligência'] = inteligencia

# Saída simples
print('-' * 70)
print('Ficha resumo do seu personagem: ')
print('=' * 70)

for atributo, entrada in personagem.items():
    print(f'{atributo}: {entrada}')
    
print()
print('Fim do programa.')