# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Colyana Magalhães da Silva Nascimento
# Data: 18/04/2024
# Atividade 001 - Operadores aritméticos

# g. Faça um programa que converta metros em centímetros e milímetros.

# Entrada
numero_em_metros = float(input('Digite um número em metros: '))

# Processamento
numero_em_centimetros = numero_em_metros * 100
numero_em_milimetros = numero_em_metros * 1000

# Saída
print(f'{numero_em_metros}m correspondem a {numero_em_centimetros}cm '
      f'e {numero_em_milimetros}mm.')