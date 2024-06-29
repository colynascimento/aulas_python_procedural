# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Colyana Magalhães da Silva Nascimento
# Data: 27/06/2024
# Aula 012 - Estruturas de Dados: Dicionarios

# C) Utilizando o exercício anterior , retire um elemento do dicionário.
import os


os.system('cls')

print('-' * 70)
print('Seja bem-vindo ao programa!')
print('Vamos criar uma ficha do seu personagem de RPG.')
print('=' * 70)

lista_personagens = []
personagem = {}

while True:
      print('MENU')
      print()
      print('1. Criar um personagem')
      print('2. Remover um personagem')
      print('3. Visualizar Personagens')
      print('4. Sair')
      print()
      
      opcao = 'Insira a sua opção (1-4):'
      
      if opcao == '1':
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

        # Adicionando ao dicionário
        personagem['nome'] = nome
        personagem['classe'] = classe
        personagem['raça'] = raca
        personagem['arma'] = arma
        
        lista_personagens.append(personagem)
        
      elif opcao == '2':
         

      # Saída simples
      print('-' * 70)
      print('Ficha resumo do seu personagem: ')
      print('=' * 70)

      for atributo, entrada in personagem.items():
      print(f'{atributo}: {entrada}')
      
      print()
      print('Fim do programa.')