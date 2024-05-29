# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Colyana Magalhães da Silva Nascimento
# Data: 28/05/2024
# Aula 009 - Comando While Else Break

import os


os.system('cls')

print('-' * 70)
print('ESTRUTURA DE CONTROLE: WHILE ELSE BREAK')
print('=' * 70)

print()

while(True):
    
    nome = str(input('Digite um nome [s - Sair]: ')).lower()
    
    if(nome != 's'):
        print('Continue digitando...')
    else:
        print('-' * 70)
        print('Você digitou "s" para sair!')
        
        break
    
print('-' * 70)
print()