# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Colyana Magalhães da Silva Nascimento
# Data: 14/05/2024
# Aula 006 - Funções Internas: Date time


#Importando as bibliotecas
import os
# Podemos importar só as funções que queremos utilizar
from datetime import datetime
from datetime import date


os.system('cls')

print('-' * 70)
print('ESTUDO DA BIBLIOTECA DATETIME')
print('-' * 70)
print()

# Declarando uma variável para data
data = datetime.now()

# Declarando uma variável formatada
data_formatada = data.strftime('%d/%m/%Y')

# Declarando uma variável data e hora formatada
data_hora_formatada = data.strftime('%d/%m/%Y %H:%M')

print(f'Data formatada: {data_formatada}')
print(f'Data e hora formatadas: {data_hora_formatada}')

# Recebendo o ano
data_atual = date.today()
nascimento = 1970
idade = data_atual.year - nascimento

# Imprimindo a data atual e o nascimento
print('-' * 70)
print(f'Data atual no sistema: {data_atual}')
print(f'Nascimento...........: {nascimento}')
# Imprimindo só o ano
print(f'Ano atual............: {data_atual.year}')
# Imprimindo só a idade
print(f'Sua idade é..........: {idade} anos')
print('-' * 70)
