# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Colyana Magalhães da Silva Nascimento
# Data: 28/05/2024
# Aula 008 - For...Range() com Validação e Casting

import os


os.system('cls')

print('-' * 70)
print('ESTRUTURA DE CONTROLE VALIDAÇÃO E CASTING')
print('=' * 70)

soma = 1

for var_iteradora in range(0, 5):
    
    numero = input('Digite um número [0-5]: ')
    
    if (not(numero.isnumeric())):
        print(f'"{numero}" Entrada inválida!')
        print()
    else:
        numero = int(numero)
        
        if(numero >= 0 and numero <= 5):
            print(f'O número {numero} está dentro do intervalo [0-5]!')
            print()
        else:
            print(f'"{numero}" Entrada inválida!')
            print()
            
print('-' * 70)
print()