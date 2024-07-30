# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Colyana Magalhães da Silva Nascimento
# Data: 30/07/2024
# Aula 012 - Estruturas de Dados: Dicionarios - Métodos Items, Keys, Values

import os


os.system('cls')

meu_dicionario = {}

while True:
  print('-' * 70)
  print('\nMenu de opções:')
  print('1. Adicionar um par chave-valor')
  print('2. Mostrar chaves do dicionário')
  print('3. Mostrar valores do dicionário')
  print('4. Mostrar itens do dicionário')
  print('5. Sair')
  print('-' * 70)

  opcao = input('Escolha uma opção (1-5): ')

  if opcao == '1':
    # Adicionar um par chav-valor ao dicionário
    chave = input('Digite a chave: ')
    valor = input('Digite o valor: ')
    meu_dicionario[chave] = valor
    print(f'Par {chave}: {valor} adicionado.')

  elif opcao == '2':
    # Mostrar as chaves do dicionário usando keys
    if meu_dicionario:
      print('Chaves do dicionário: ', meu_dicionario.keys())
    else:
      print('O dicionário está vazio. Adicione itens primeiro.')

  elif opcao == '3':
    print('Saindo do programa.')
    break
  else:
    print('Opção inválida. Tente Novamente.')


