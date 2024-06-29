# Trabalho sobre a estrutura de dados SET
# Senac Minas Gerais/Juiz de Fora
# Aluna: Colyana Magalhães da Silva Nascimento
# Turma 0152
# Data: 24/06/2024

# Estrutura de Dados: Método Intersection/&

# Esse é um programa que tem por objetivo automatizar a agenda de um tatuador.
# As pessoas podem marcar a tatuagem pelo Whatsapp, ou pelo seu programa, e esse
# programa verifica se o dia que o cliente está tentando agendar já está ocupado.


import os


os.system('cls')

print('-' * 70)
print('Seja bem-vindo ao programa!')
print('Vamos agendar uma tatuagem no Studio Ink Tattoo')
print('=' * 70)

print('Está aberta a agenda do mês de Julho!')
print('OBSERVAÇÃO! Não agendamos aos domingos.')
print()
novo_agendamento = input('Qual dia do mês de julho você deseja agendar? ')

# Dias ocupados
agenda_whatsapp_julho = {'1', '2', '5', '6', '14', '15', '19', '27'}
agenda_julho = {'4', '10', '18', '20', '21', '25', '28'}
domingos_julho = {'7', '14', '21', '28'} 

agenda_julho.append(novo_agendamento)


