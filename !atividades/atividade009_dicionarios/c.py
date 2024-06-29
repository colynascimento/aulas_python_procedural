# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Colyana Magalhães da Silva Nascimento
# Data: 27/06/2024
# Aula 012 - Estruturas de Dados: Dicionarios

# C) Utilizando o exercício anterior , retire um elemento do dicionário.
import os
import random


os.system('cls')

print('-' * 70)
print('Seja bem-vindo ao programa!')
print('Vamos criar uma ficha do seu personagem de RPG.')
print('=' * 70)

lista_personagens = []

while True:
        print('MENU')
        print()
        print('1. Criar um personagem')
        print('2. Remover um personagem')
        print('3. Visualizar Ficha dos Personagens')
        print('4. Sair')
        print()
      
        opcao = input('Insira a sua opção (1-4): ')
      
        if opcao == '1':
                novo_personagem = {}
                # Atribuindo valores
                print()
                print('-' * 70)
                print('Criar um novo personagem')
                print()
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
                novo_personagem['nome'] = nome
                novo_personagem['classe'] = classe
                novo_personagem['raça'] = raca
                novo_personagem['arma'] = arma
                novo_personagem['força'] = forca
                novo_personagem['inteligência'] = inteligencia
                
                lista_personagens.append(novo_personagem)
                
                print(lista_personagens)
                
                print(f'Personagem {nome.capitalize} criado!')
                print('-' * 70)
                print()
        
        elif opcao == '2':
                os.system('cls')
                
                print('Remover personagem')
                print('Personagens disponíveis:')
                print()
                for i, personagem in enumerate(lista_personagens):
                        numeracao = i + 1
                        print(f'{numeracao}- {personagem['nome']}')
                        
                remover_personagem = input('Digite o número do personagem que deseja remover: ')
                        
                if remover_personagem.isdigit() == False:
                        print('Digite apenas o número do personagem.')
                        print()
                elif 0 < int(remover_personagem) <= len(lista_personagens):
                        personagem_removido = lista_personagens.pop(int(remover_personagem) - 1)
                        print(f'Personagem {personagem_removido['nome']} removido com sucesso!')
                        input('\nPressione Enter para voltar ao Menu...')
                        print()
                else:
                        print('\nNúmero inválido.')
                        print()
                        
        elif opcao == '3':
                        
                print('-' * 70)
                print('Ficha resumo dos seus personagens: ')
                print('=' * 70)
                print()

                for personagem in lista_personagens:
                        for atributo, entrada in personagem.items():
                                print(f'{atributo}: {entrada}')
                        print()
                input('\nPressione Enter para voltar ao Menu...')
                print()
        
        elif opcao == '4':
                print('Saindo do programa.')
                break
    
        else:
                input('Opção inválida. Enter para tentar novamente...')        