# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Colyana Magalhães da Silva Nascimento
# Data: 15/04/2024
# Variáveis em Python

# Importando as bibliotecas (depois da importação tem que pular 2 linhas)
import os


os.system('cls')

# As variáveis são calculadas por inferência, pois o Python é uma linguagem de baixa tipagem
nome = 'Colyana'
nascimento = 2000
altura = 1.63
peso = 49.5
doador = True
complexo = 3j  # Python trabalha diretamente com números complexos
PI = 3.14  # Isso é uma CONSTANTE, seu valor não deve ser alterado

numeros = [1, 2, 3, 4, 5]
meses_do_ano = ('Janeiro', 'Fevereiro', 'Março')
aluno = {'nome': 'Coly', 'idade': 24, 'nota': 10.0}
numeros_primos = {2, 3, 5, 7, 11}

# Saída utilizando o método type( para verificar o tipo da variável)
print('-' * 70)
print('\033[0m \033[31mTipos declarados:\033[0m')
print('=' * 70)
print('\033[0m A var \033[32nome \033[0m é do tipo: ', type(nome))
print('\033[0m A var \033[32m nascimento \033[0m é do tipo: ', type(nascimento))
print('\033[0m A var \033[32m altura \033[0m é do tipo: ', type(altura))
print('\033[0m A var \033[32m peso \033[0m é do tipo: ', type(peso))
print('\033[0m A var \033[32m doador \033[0m é do tipo: ', type(doador))
print('\033[0m A var \033[32m complexo \033[0m é do tipo: ', type(complexo))
print('\033[0m A var \033[32m PI \033[0m é do tipo: ', type(PI))
print('\033[0m A var \033[32m numeros \033[0m é do tipo: ', type(numeros))
print('\033[0m A var \033[32m meses_do_ano \033[0m é do tipo: ', type(meses_do_ano))
print('\033[0m A var \033[32m aluno \033[0m é do tipo: ', type(aluno))
print('\033[0m A var \033[32m numeros_primos \033[0m é do tipo: ', type(numeros_primos))
print('-' * 70)
print('')
