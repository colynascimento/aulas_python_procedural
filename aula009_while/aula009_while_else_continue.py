# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Colyana Magalhães da Silva Nascimento
# Data: 28/05/2024
# Aula 009 - Comando While... Else... Continue

import os


os.system('cls')

print('-' * 70)
print('ESTRUTURA DE CONTROLE: WHILE ELSE CONTINUE')
print('=' * 70)

print()

contador = 0 # Flag

while (contador <= 10):
    
    contador +=1
    
    if contador % 2 == 0: # pulando os pares
        continue
    print(f'Contador = {contador}')
else:
    print(f'Bloco do While...Else: contador em {contador}!')
        
print('-' * 70)
print('Fim do programa!')
print()