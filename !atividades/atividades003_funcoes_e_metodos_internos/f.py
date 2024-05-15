# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Colyana Magalhães da Silva Nascimento
# Data: 14/05/2024
# Atividade 003: Funções/Métodos Internos

# F) Faça um programa onde o usuário tenta adivinhar o número que o
# computador está ‘pensando’.
# Vou considerar um valor de 0 a 100

import os
import random

os.system('cls')

print('-' * 70)
print('ATIVIDADE 3: Questão F')
print('Adivinhe o número que o computador está pensando!')
print('=' * 70)

# Recebendo o valor do usuário
valor_usuario = int(input('Insira o valor inteiro que você acha que o computador está pensando: '))
valor_computador = random.randint(0, 100)

# Verificação e saída
if valor_usuario == valor_computador:
    print(f"Parabéns! Você conseguiu acertar, o computador estava pensando em {valor_usuario}")
else:
    print(f"Poxa! Você errou, na verdade o computador estava pensando em {valor_computador}, não em {valor_usuario}.\n"
          f"Mas não desista, tente novamente!")
print('-' * 70)
print()