# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Colyana Magalhães da Silva Nascimento
# Data: 17/06/2024
# Atividade 007: Listas

# G) Faça um programa que sorteia os números da Mega Sena e da
# Lotofácil.

import os
import random


os.system('cls')

print('-' * 70)
print('Seja bem vindo a Fortuna da Sorte!')
print('Vamos sortear os números da Mega Sena e Lotofácil.')
print('=' * 70)

megasena = []
lotofacil = []

for i in range(6):
    numero = random.randint(1, 60)
    megasena.append(numero)
    
for i in range(15):
    numero = random.randint(1, 25)
    lotofacil.append(numero)

print('Primeiro... O sorteio da Mega Sena!')
print('Os números sorteados foram:')

for numero in megasena:
    print(numero, end='\n')
    
print('')
print('Você acertou algum?')
print('Senão, não desanime...')
print('Agora vamos sortear os número da Lotofácil!')
print('Boa sorte!')
print('Lá vai:')

for numero in lotofacil:
    print(numero, end='\n')
    
print('-' * 70)
print('Fim do sorteio')
print('')