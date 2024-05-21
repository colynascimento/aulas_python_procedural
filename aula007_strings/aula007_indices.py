# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Colyana Magalhães da Silva Nascimento
# Data: 20/05/2024
# Aula 007 - Fatiamento de Strings

import os


os.system('cls')

print('-' * 70)
print('Fatiamento de Strings')
print('=' * 70)

frase = 'String em Python!'

# Exibindo a string original
print(f'String original: {frase}\n')

# Fatiamento: acessando partes específicas da String
# Primeiros cinco caracteres
primeiros_cinco = frase[:5]
print(f'Primeiros cinco caracteres: {primeiros_cinco}\n')

# Últimos dez caracteres
ultimos_dez = frase[-10:]
print(f'Últimos dez caracteres: {ultimos_dez}\n')

# Do quarto ao último caractere
quarto_ao_decimo = frase[3:10]
print(f'Do quarto ao décimo caractere: {quarto_ao_decimo}\n')

# A cada dois caracteres
a_cada_dois = frase[::2]
print(f'A cada dois caracteres: {a_cada_dois}\n')

# Invertendo a string
invertida = frase[::-1]
print(f'String invertida: {invertida}\n')