# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Colyana Magalhães da Silva Nascimento
# Data: 28/05/2024
# Aula 008 - For...Range() Break

import os


os.system('cls')

print('-' * 70)
print('ESTRUTURA DE CONTROLE: BREAK')
print('=' * 70)

print()

for var_iteradora in range(0, 10):
    
    print(f'Valor: {var_iteradora}')
    
    if (var_iteradora == 5):
        print(f'Contagem interrompida no {var_iteradora}')
        break
    
print('-' * 70)
print('Fim do Programa!')
print()