# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Colyana Magalhães da Silva Nascimento
# Data: 17/06/2024
# Atividade 007: Listas

# A) Faça um programa que leia um número indeterminado de notas
# (pressione ‘s’ ou ‘0’ para sair). Após esta entrada de dados,
# faça o seguinte:

# • Mostre a quantidade de notas que foram lidas.
# • Exiba todas as notas na ordem em que foram informadas.
# • Exiba todas as notas na ordem inversa à que foram informadas, uma abaixo da outra.
# • Calcule e mostre a soma das notas.
# • Calcule e mostre a média das notas.

import os


os.system('cls')

print('-' * 70)
print('Seja bem-vindo ao programa!')
print('Vams analisar as notas dos alunos.')
print('=' * 70)

i = 1
soma = 0
lista_notas = []

while True:
    
    nota = input(f'Insira a {i}º nota [ou digite "s" para encerrar]: ')
    
    if nota == 's':
        break
    else:
        nota = float(nota)
        lista_notas.append(nota)
        
    
    i += 1
    soma += nota
    

quantidade_notas = i - 1
media = soma / quantidade_notas


print('') 
print(f'Foram lidas {quantidade_notas} notas no total.')
print(f'As notas informadas foram: {lista_notas}')

print(f'Já as notas na ordem inversa ficam: ')
lista_notas.reverse()
for nota in range(len(lista_notas)):
    print(lista_notas[nota], end='\n')
    
print(f'A soma de todas as notas é: {soma}')
print(f'A média de notas dos alunos é: {media:.2f}')

print('-' * 70)
print('Fim do programa!')
print('')