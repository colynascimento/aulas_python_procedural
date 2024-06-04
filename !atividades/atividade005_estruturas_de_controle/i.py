# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Colyana Magalhães da Silva Nascimento
# Data: 28/05/2024
# Atividade 005: Estruturas de Controle

# I) Faça um algoritmo que imprima a frase "estou em looping" e, em 
# seguida, solicite ao usuário digitar uma letra. Caso a letra seja 
# o “f" finalize a aplicação. Do contrário, imprima novamente a mesma
# frase até que o caractere “f" seja digitado.

import os


os.system('cls')

while True:
    
    letra = input('Digite uma letra: ').lower()
    
    if letra != 'f':
        print('Tente novamente!')
        print(input('Digite uma letra: ').lower())
    else:
        print('-' * 70)
        print('Você digitou "F" para sair!')
        
        break