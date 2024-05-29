# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Colyana Magalhães da Silva Nascimento
# Data: 28/05/2024
# Aula 009 - While... Else

import os


os.system('cls')

print('-' * 70)
print('ESTRUTURA DE CONTROLE: WHILE... ELSE')
print('=' * 70)

print()

contador = 1

while contador < 7:
    print('Contador é: ', contador)
    contador +=1
    
    # Se eu tirar essa condicional o else será executado
    if contador == 4:
        print(f'Contador chegou em {contador}. Break no While!')
        break
else:
    print('While finalizado!')
    
print('-' * 70)
print('Fim do programa!')
print()